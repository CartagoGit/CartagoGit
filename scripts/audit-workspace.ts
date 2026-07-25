#!/usr/bin/env bun

import { readdir, readFile, stat } from "node:fs/promises";
import { join, relative, resolve } from "node:path";

type PackageManifest = {
  name?: string;
  description?: string;
  scripts?: Record<string, string>;
  dependencies?: Record<string, string>;
  devDependencies?: Record<string, string>;
};

type Project = {
  path: string;
  category: "company" | "personal";
  manifests: string[];
  package?: Pick<PackageManifest, "name" | "description">;
  scripts: string[];
  dependencies: string[];
  readme: boolean;
};

const workspace = resolve(process.argv[2] ?? "..");
const rootName = "CartagoGit";
const ignored = new Set([".git", "node_modules", "vendor", "dist", "build", ".angular", ".next"]);

async function findRepositories(directory: string): Promise<string[]> {
  const entries = await readdir(directory, { withFileTypes: true });
  if (entries.some((entry) => entry.isDirectory() && entry.name === ".git")) return [directory];

  const nested = await Promise.all(
    entries
      .filter((entry) => entry.isDirectory() && !ignored.has(entry.name))
      .map((entry) => findRepositories(join(directory, entry.name))),
  );
  return nested.flat();
}

async function exists(path: string): Promise<boolean> {
  try {
    return (await stat(path)).isFile();
  } catch {
    return false;
  }
}

async function auditProject(projectPath: string): Promise<Project> {
  const packagePath = join(projectPath, "package.json");
  const hasPackage = await exists(packagePath);
  const manifestCandidates = ["package.json", "composer.json", "pyproject.toml", "go.mod", "Cargo.toml"];
  const manifests = await Promise.all(
    manifestCandidates.map(async (name) => ((await exists(join(projectPath, name))) ? name : undefined)),
  );

  let manifest: PackageManifest | undefined;
  if (hasPackage) manifest = JSON.parse(await readFile(packagePath, "utf8")) as PackageManifest;

  const path = relative(workspace, projectPath) || rootName;
  return {
    path,
    category: path === "Beateam" || path.startsWith("Beateam/") ? "company" : "personal",
    manifests: manifests.filter((value): value is string => Boolean(value)),
    package: manifest && { name: manifest.name, description: manifest.description },
    scripts: Object.keys(manifest?.scripts ?? {}).sort(),
    dependencies: Object.keys({ ...manifest?.dependencies, ...manifest?.devDependencies }).sort(),
    readme: await exists(join(projectPath, "README.md")),
  };
}

const repositories = await findRepositories(workspace);
const projects = await Promise.all(repositories.map(auditProject));
projects.sort((left, right) => left.path.localeCompare(right.path));

console.log(JSON.stringify({ workspace, generatedAt: new Date().toISOString(), projects }, null, 2));
