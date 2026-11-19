# Curacion del perfil publico

## Objetivo

El perfil debe presentar a Mario como ingeniero full-stack de TypeScript que construye
herramientas de desarrollo, infraestructura de IA y software de producto, y que lo hace con
disciplina de ingenieria verificable.

Dos reglas gobiernan todo lo que hay aqui:

1. **El trabajo se describe por la capacidad que demuestra, no por el nombre del producto.**
   Los productos cambian de nombre con frecuencia — `mcp-vertex` hoy es `DelendAI` — y una pagina
   atada a un nombre caduca. La capacidad no caduca; solo cambia el enlace.
2. **Solo se afirma lo comprobable.** Las metricas estan medidas sobre los repositorios
   publicos. Los badges y las graficas refuerzan informacion verificable; no la sustituyen.

La experiencia profesional se refleja por capacidades, no por nombres de clientes, repositorios
internos, capturas, datos de dominio ni fragmentos de codigo corporativo.

## Inventario medido

Medido sobre los repositorios publicos, con los tests excluidos de las lineas de codigo:

| Repositorio | Commits | Lineas de codigo | Lineas de test | Ficheros de test | Paquetes |
| --- | ---: | ---: | ---: | ---: | ---: |
| DelendAI | 17.484 | 628.712 | 460.854 | 2.709 | 84 |
| api-source-tanit | 1.876 | 99.398 | 73.489 | 362 | 53 |
| quickmodel | 550 | 58.636 | 100.258 | 407 | 1 |
| player-club-dynasty | 294 | 36.041 | 13.628 | 9 | 2 |
| steam-keys | 117 | 33.518 | 11.462 | 50 | 2 |
| aoe2-mods | 1.123 | 31.838 | 7.382 | 19 | 1 |
| portfolio | 162 | 6.352 | 1.047 | 21 | 2 |
| print-cv | 132 | 2.179 | 230 | 7 | 1 |

## Repositorios visibles

El perfil publica 26 repositorios visibles. Todos tienen descripcion de una frase y topicos.

### Fijados

El orden lo fija Mario por importancia, uso y visibilidad potencial:

1. `DelendAI` — nucleo de servidor MCP y CLI de plugins. Es la pieza con mas profundidad tecnica.
2. `api-source-tanit` — descubrimiento de API desde codigo fuente. 25 frameworks.
3. `quickmodel` — libreria de serializacion de modelos TypeScript, publicada en npm.
4. `DockerNodeBun` — imagen de desarrollo Node + Bun, la mas descargada.
5. `Keyer` — CLI y libreria publicada en npm para cifrar secretos y `.env`.
6. `print-cv` — aplicacion Vue/TypeScript con tests de extremo a extremo, desplegada en Pages.

### Publicos, no fijados

`CartagoGit`, `CartagoGit.github.io`, `portfolio`, `steam-keys`, `aoe2-mods`,
`player-club-dynasty`, `ReactGpt`, `NestGpt`, `zoneless-calculator`, `template-angular`,
`codember-dev`, `codewars`, `parse-xml-json`, `script-comparar-csv`, `tablon-tareas-cartago`,
`DockerZsh`, `DockerAngular`, `DockerIonicCover`, `DockerNestJsCover`.

## Repositorios publicados desde privado

Tres repositorios con trabajo solido pasan de privado a publico. La decision se tomo despues de
auditar secretos y datos personales:

| Repositorio | Tamano | Publicacion | Motivo |
| --- | ---: | --- | --- |
| `steam-keys` | 2,9 MB | publica | Producto local-first de escritorio (Tauri 2, Rust, SQLite). El `.gitignore` excluye claves, base de datos y exportaciones, y el README lo documenta. |
| `aoe2-mods` | 91 MB | publica | Fabrica de contenido con pipeline TS + Python, i18n en/es-ES y licencia de contenido separada. Es el proyecto de modding mas serio. |
| `player-club-dynasty` | 41 MB | publica | Simulador de gestor de futbol en Godot/C# construido con un pipeline de entrega asistido por IA. 1.217 ficheros versionados. |

`porra`, `clear-accounts`, `horas-mario-2025`, `affairs` y `deathblitz` siguen privados: `porra`
contiene datos de personas reales en su dataset y `deathblitz` declara propiedad privada.

## Repositorios archivados

Archivar conserva el codigo y comunica que ya no recibe mantenimiento. Se archivaron 40
repositorios:

- **Material de curso** (Angular, Laravel, Solidity, Flutter, RxJS, NGRX, CSS, VS Code, Docker,
  Solid, JavaScript): `Curso-*`, `curso-*`, `*-por-fernando-herrera`, `*-por-Fernando-Herrera`,
  `Angular-Avanzado-*`, `Angular-14-*`, `css-complete-guide`, `CryptoZombies`,
  `cursos-solidity`, `Flutter-Movil_cero_a_experto`, `design-web-profesional-curso`,
  `docker-graphql`.
- **Juegos y ejercicios sueltos**: `chess`, `snake`, `tetris`, `minesweeper`, `tic-tac-toe-react-page-tutorial-in-ts`,
  `todo-list-react-vite-ts`, `counter-redux-vite-ts`, `chatApp-nodejs-socketio`, `CryptoEconomy`.
- **Copias y material incompleto**: `portafolios-cartago`, `portafolios-cartago-api`,
  `sdkward`, `ngx-cartago-lib`, `basico_php`, `tutorial-storybook-angular`,
  `fork--turbo-console-log--afterdelimitter`, `Cartago-CoinGecko_NodeJs-serverless`.
- `Certificados` se privatizo: son credenciales personales, no codigo.

## Repositorios con trabajo real que estaban escondidos

`print-cv` tenia su implementacion —validacion Zod, i18n en/es, modo impresion, tests de
Playwright— en la rama `mejorar-con-implementaciones-para-nuevo-cv`, mientras `main` conservaba
el README de la plantilla de Vue. La rama se integro en `main` con un fast-forward: 36 commits,
154 ficheros, 4.933 lineas anadidas. El README tambien se reescribio.

## Productos visitables

| Producto | URL | Estado |
| --- | --- | --- |
| Portfolio estatico | https://cartagogit.github.io | activo, en `CartagoGit.github.io` |
| Print CV | https://cartagogit.github.io/print-cv/ | activo, desplegado por `deploy.yml` |
| Documentacion de QuickModel | https://cartagogit.github.io/quickmodel/ | activo |
| Documentacion de DelendAI | https://cartagogit.github.io/DelendAI/ | pendiente: `pages.yml` solo se dispara en `main`, que va 9.898 commits por detrás de `develop` |

`tanit.dev` no es de este proyecto: es un producto blockchain distinto. No enlazarlo.

## Enlaces con nombre obsoleto

`https://github.com/CartagoGit/mcp-vertex` redirige a `DelendAI`, asi que los enlaces antiguos
siguen funcionando. Aun asi, el README del perfil y el de `portfolio` usan ya el nombre actual.

En `portfolio` quedan intactos los nombres locales reales —`mcp-vertex.config.json`,
`docs/mcp-vertex/`, `check-mcp-vertex.mjs`, `file:../mcp-vertex/packages/core`— porque renombrarlos
es un cambio de codigo, no de documentacion.

## Ajustes del perfil de GitHub

- Nombre: `Mario Cabrero Volarich` — **pendiente**: el token actual no tiene el permiso `user`.
- Bio: `Full-stack TypeScript engineer. Developer tooling, AI infrastructure and product
  software: MCP runtimes, static analysis, typed libraries, desktop apps.` — **pendiente**, mismo
  motivo.
- Ubicacion: `Sevilla, Spain` — ya correcta.
- Website: `https://cartagogit.github.io` — **pendiente**, mismo motivo.
- El bloque `GitHub Activity` va **desplegado**: es la unica prueba de actividad reciente y un
  desplegable la esconde.

## Iconos

Cada producto usa su propia marca, no un emoji ni un avatar generico:

| Fichero | Origen |
| --- | --- |
| `assets/delendai.svg` | `apps/shared/brand/logo.svg` de DelendAI (el mismo hexagono que antes se llamaba `mcp-vertex.svg`) |
| `assets/tanit.png` | `packages/desktop/icons/icon.png` de api-source-tanit, escalado a 256 px |
| `assets/quickmodel.png` | `assets/quickmodel.png` de quickmodel |
| `assets/steam-keys.png` | `apps/desktop/public/favicon.png` de steam-keys, escalado a 512 px |
| `assets/portfolio.png` | `public/favicon.ico` de portfolio, escalado a 256 px |
| `assets/print-cv.svg` | marca propia: una hoja con lineas de texto en el verde del producto (`#3cb878`) |

El favicon de print-cv es un icono de Font Awesome con licencia CC BY 4.0; no se copia al
perfil. Se dibuja una marca equivalente en SVG propio.

`assets/mcp-vertex.svg` se elimino: el producto ya no se llama asi y su logo esta en
`assets/delendai.svg`.

## Mantenimiento por repositorio

Todo repositorio publico que se mantenga debe tener como minimo:

1. Una descripcion de GitHub de una frase y de 3 a 5 temas relevantes.
2. Un README con problema, alcance, arquitectura, requisitos, comandos de ejecucion con Bun cuando aplique, pruebas y estado.
3. Un `LICENSE` adecuado y `.gitignore` sin secretos, binarios locales, archivos de agentes ni resultados de pruebas.
4. Una decision explicita: activo, mantenido, archivado o privado.

Los README reparados en esta pasada:

| Repositorio | Que estaba mal |
| --- | --- |
| `CartagoGit` | Describia `mcp-vertex` como producto actual y no tenia metricas. Reescrito por capacidades, con iconos y evidencia medida. |
| `CartagoGit.github.io` | Posicionamiento de "frontend" y un icono que apuntaba a un repositorio renombrado. Reescrito y alineado. |
| `print-cv` | El README de la plantilla de Vue. Sustituido por el real, con el estado del proyecto, los comandos y la estructura. |
| `zoneless-calculator` | Notas de instalacion de Chrome en WSL2. Sustituido por un README que explica la decision zoneless y sus tests. |
| `NestGpt` | Solo instrucciones de instalacion y un enlace a otro repositorio. Sustituido por un README con los endpoints, los DTOs y los comandos. |
| `portfolio` | Nombres obsoletos (`mcp-vertex`) y posicionamiento antiguo en el titulo y la meta descripcion. Actualizado. |
| `api-source-tanit` | La descripcion de GitHub decia 21 frameworks; el README dice 25. Corregida. |

## Trabajo pendiente

1. **Permiso `user` en el token.** Sin el, el nombre, la bio y la web del perfil no se pueden
   cambiar por API. El token actual es un fine-grained PAT sin ese permiso.
2. **Permiso `pinRepository`.** La mutacion de GraphQL no existe en el schema publico; fijar
   repositorios se hace desde la interfaz. Los fijados actuales ya estan en el orden que eligio
   Mario.
3. **Documentacion de DelendAI.** `pages.yml` solo se dispara en `main`. Hay que decidir si el
   sitio se publica desde `develop` (lo natural, porque es donde vive el codigo) o si `main` debe
   recibir merges periodicos. El repositorio impone su propia gobernanza de ramas y propuestas,
   asi que la decision es de Mario.
4. **Repositorios pequenos sin README**: `parse-xml-json`, `script-comparar-csv`,
   `tablon-tareas-cartago`, `codember-dev` y `codewars`. Son utiles, pero con un README minimo
   —problema, uso y estado— o archivados.
