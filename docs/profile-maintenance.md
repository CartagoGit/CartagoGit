# Mantenimiento del perfil

Los scripts del repositorio se escriben en TypeScript y se ejecutan con Bun.

## Auditoria local

Genera un inventario JSON de los repositorios del workspace, sus manifiestos, scripts y dependencias. El informe se imprime por salida estandar; no guarda ni publica informacion corporativa.

```console
bun scripts/audit-workspace.ts /home/cartago/_projects
```

## Licencias MIT

`add-mit-license-all-repositories.ts` sustituye el antiguo script Bash. Consulta los repositorios propios mediante la API de GitHub y, por defecto, solo muestra las acciones previstas.

```console
OWN_GITHUB_TOKEN=... bun scripts/add-mit-license-all-repositories.ts --workspace=/ruta/a/repositorios
```

La escritura, commit y push requieren `--apply` de forma explicita:

```console
OWN_GITHUB_TOKEN=... bun scripts/add-mit-license-all-repositories.ts --workspace=/ruta/a/repositorios --apply
```

Usar un token con acceso de escritura solo cuando se quiera aplicar el cambio. El script omite repositorios que ya contienen `LICENSE`.
