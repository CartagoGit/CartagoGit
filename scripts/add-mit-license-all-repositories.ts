#!/usr/bin/env bun

import { mkdir, writeFile } from "node:fs/promises";
import { basename, join, resolve } from "node:path";

const token = process.env.OWN_GITHUB_TOKEN ?? process.env.GITHUB_TOKEN;
const apply = process.argv.includes("--apply");
const workspace = resolve(process.argv.find((argument) => argument.startsWith("--workspace="))?.slice(12) ?? ".");
const year = new Date().getFullYear();
const owner = "Mario Cabrero Volarich as Cartago";

if (process.argv.includes("--help")) {
  console.log("Usage: OWN_GITHUB_TOKEN=... bun scripts/add-mit-license-all-repositories.ts [--workspace=PATH] [--apply]");
  process.exit(0);
}

if (!token) throw new Error("Set OWN_GITHUB_TOKEN (or GITHUB_TOKEN) before running this script.");

const license = `MIT License

Copyright (c) ${year} ${owner}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the \"Software\"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
`;

async function run(command: string[], cwd = workspace): Promise<string> {
  const process = Bun.spawn(command, { cwd, stdout: "pipe", stderr: "pipe" });
  const [stdout, stderr, exitCode] = await Promise.all([
    new Response(process.stdout).text(),
    new Response(process.stderr).text(),
    process.exited,
  ]);
  if (exitCode !== 0) throw new Error(`${command.join(" ")} failed: ${stderr.trim()}`);
  return stdout.trim();
}

const response = await fetch("https://api.github.com/user/repos?per_page=100&affiliation=owner", {
  headers: { Accept: "application/vnd.github+json", Authorization: `Bearer ${token}` },
});
if (!response.ok) throw new Error(`GitHub API request failed: ${response.status} ${response.statusText}`);

const repositories = (await response.json()) as Array<{ clone_url: string; full_name: string; name: string }>;
for (const repository of repositories) {
  const directory = join(workspace, basename(repository.name));
  const licensePath = join(directory, "LICENSE");
  const exists = await Bun.file(licensePath).exists();

  if (exists) {
    console.log(`skip  ${repository.full_name}: LICENSE already exists`);
    continue;
  }

  if (!apply) {
    console.log(`would add MIT license: ${repository.full_name}`);
    continue;
  }

  if (!(await Bun.file(join(directory, ".git")).exists())) {
    await mkdir(directory, { recursive: true });
    await run(["git", "clone", repository.clone_url, directory]);
  }

  await writeFile(licensePath, license, "utf8");
  await run(["git", "add", "LICENSE"], directory);
  await run(["git", "commit", "-m", "Add MIT License"], directory);
  await run(["git", "push"], directory);
  console.log(`added MIT license: ${repository.full_name}`);
}
