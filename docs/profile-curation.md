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

Cada producto usa su propia marca. **No se envuelven en una ficha**: el logo de DelendAI y el
de QuickModel ya son marcas completas y anadirles un fondo los deforma. Los que no tenian marca
propia (Keyer, Print CV, Cartago) si llevan la suya, dibujada para leerse a 16 px.

| Fichero | Origen |
| --- | --- |
| `assets/delendai.svg` | El logo original de DelendAI (`apps/shared/brand/logo.svg`), sin tocar. |
| `assets/tanit.svg` | **La marca del autor:** la diosa con el tocado radiado, en terracota `#da5b33` sobre verde azulado `#04343d`. |
| `assets/quickmodel.png` | `assets/quickmodel.png` de quickmodel, sin tocar. |
| `assets/print-cv.svg` | **Marca nueva.** Una hoja con lineas de texto y el pliegue, en el verde del producto (`#3cb878`). |
| `assets/cartago.svg` | **Marca nueva.** El monograma "C." sobre un disco azul, que es el logo del portfolio y su favicon. |
| `assets/keyer.svg` | **Marca nueva.** Una llave de laton sobre azul marino, para el paquete de secretos. |
| `assets/docker.svg` | La ballena de Docker con sus contenedores, para la tarjeta de imagenes. |
| `assets/steam-keys.png` | El favicon real de la aplicacion, dentro de una ficha. |

**Steam Keys no aparece en las tarjetas destacadas del perfil**: el producto que se publica es
**Keyer**, con enlace a npm. En el sitio estatico si aparece, con su icono real.

### Iconos de destino

Cada enlace dice adonde lleva con el icono de lo que es, no con la palabra suelta:

| Destino | Icono | Fichero |
| --- | --- | --- |
| Repositorio | El logotipo de GitHub | `assets/github.svg` |
| Releases | Una etiqueta | `assets/releases.svg` |
| Documentación | Un libro | `assets/docs.svg` |
| Aplicación en vivo | Un globo | `assets/live.svg` |
| Paquete npm | Una caja | `assets/package.svg` |

Los cuatro últimos vienen de Iconify en blanco y azul (`mdi:tag`, `mdi:book-open-variant`,
`mdi:earth`, `mdi:package-variant`) con el color explicito, porque `currentColor` no se
resuelve dentro de un `<img>`.

**Ojo con `width="1em"`:** los SVG de Iconify lo traen, y GitHub escala entonces el icono al
tamano de la linea, con lo que queda casi invisible junto a la etiqueta. Se quita el atributo y
manda el `width` del `img`.

Los iconos del repositorio del perfil y los del sitio estatico son el mismo juego: asi una
marca no cambia de aspecto depending de donde aparezca.

Los logotipos que eran PNG se embeben dentro de la ficha SVG, cuantizados a 128 colores: el
repositorio del perfil pesa unos pocos kilobytes por icono en vez de varios megabytes.

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
| `portfolio` | Nombres obsoletos (`mcp-vertex`) y posicionamiento antiguo en el titulo y la meta descripcion. Actualizado. Ademas, el favicon era el logo de Angular: ahora es el monograma "C." del sitio. |
| `api-source-tanit` | La descripcion de GitHub decia 21 frameworks; el README dice 25. Corregida. |

## El sitio estatico

`CartagoGit.github.io` se rehizo sobre un unico conjunto de tokens —color, tipografia, escala de
espaciado y de radios— para que todas las secciones esten espaciadas igual. Cambios:

- La ficha de marca del encabezado es ahora el monograma "C." y el favicon es el mismo fichero.
- Las tarjetas de proyecto ponen el icono **encima** del titulo, para que el icono pertenezca al
  producto y no flote a la izquierda del texto.
- Los enlaces a GitHub, LinkedIn, npm y Docker Hub estan como enlaces con icono SVG.
- El bloque de contacto es una tarjeta coral, para que el final de la pagina tenga peso.
- Se anadieron los enlaces reales a los productos que funcionan: la app de Print CV y la
  documentacion de QuickModel.

El sitio sigue sin dependencias: se publica desde `main` tal cual en GitHub Pages.

## Trabajo pendiente

1. **Permiso `user` en el token.** Sin el, el nombre, la bio y la web del perfil no se pueden
   cambiar por API. El token actual es un fine-grained PAT sin ese permiso.
2. **Permiso `pinRepository`.** La mutacion de GraphQL no existe en el schema publico; fijar
   repositorios se hace desde la interfaz. Los fijados actuales ya estan en el orden que eligio
   Mario.
3. **Documentacion de DelendAI.** `pages.yml` solo se dispara en `main`. Hay que decidir si el
   sitio se publica desde `develop` (lo natural, porque es donde vive el codigo) o si `main` debe
   recibir merges periodicos. El repositorio impone su propia gobernanza de ramas y propuestas,
   asi que la decision es de Mario. La propuesta `x01103` esta escrita y pasa el linter.
4. **Repositorios pequenos sin README**: `parse-xml-json`, `script-comparar-csv`,
   `tablon-tareas-cartago`, `codember-dev` y `codewars`. Son utiles, pero con un README minimo
   —problema, uso y estado— o archivados.
5. **Logo y banner definitivos del portfolio.** Pendiente de que se entregue la marca; el sitio
   usa ahora el monograma "C." y el banner `banner-03-neon.png`.

## Servicios de badges del README

Comprobado el 2026-11-20. El servicio publico `github-readme-stats.vercel.app` devuelve un
error 500 (`FUNCTION_INVOCATION_FAILED`), asi que el enlace salia roto. Se cambio por el espejo
`github-readme-stats-fast.vercel.app`, que responde 200 con SVG valido.

Los otros dos si funcionan:

| Servicio | Estado |
| --- | --- |
| `github-readme-activity-graph.vercel.app` | correcto, devuelve SVG |
| `streak-stats.demolab.com` | correcto |
| `github-readme-stats.vercel.app` | **error 500**, sustituido por el espejo `-fast` |

Si el espejo tambien cae, la alternativa honesta es quitar el badge y dejar solo el grafico de
actividad y la racha, que ya demuestran la actividad reciente.
