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
| `assets/cartago.svg` | **Marca entregada por Mario.** El globo con continentes azules; sustituye al monograma "C." en el encabezado, en la tarjeta del portfolio y en el favicon. |
| `assets/cartago-banner.png` | **Banner entregado por Mario.** El mismo globo sobre azul marino. Va **sin tocar**: no se procesa, no se recorta ni se recolorea. |
| `assets/keyer.svg` | **Marca nueva.** Una llave de laton sobre azul marino, para el paquete de secretos. |
| `assets/docker.svg` | La ballena de Docker con sus contenedores, para la tarjeta de imagenes. |
| `assets/brand/steam-keys.svg` | El favicon real de la aplicacion, junto al resto de marcas del sitio. |
| `assets/brand/mods.svg` | Puzzle de Iconify (`mdi:puzzle`), para la tarjeta de fabricacion de mods. |

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

### El color de los iconos

El bug que se veia: los iconos del encabezado del portafolio eran blancos sobre fondo claro,
y los del stack salian todos blancos porque el CSS los forzaba con
`filter: brightness(0) invert(1)` para que se vieran en oscuro. Un filtro no puede saber el
color de la marca, asi que todos quedaban del mismo color.

La solucion tiene dos partes:

1. **El color va en el fichero.** `scripts/normalize-brand-icons.py` escribe el color de la
   marca en el `<svg>` raiz y quita los `fill` de los `path` **solo en el cuerpo** (si se
   quitan en todo el fichero, se borra el que se acaba de poner). Angular sale rojo, Vue
   verde, React azul claro, Sass rosa. Se ejecuta sobre `assets/brand` de los dos repos.
2. **En el sitio no hay ficha.** Los iconos pequenos van directos, mas grandes (16–19 px),
   sobre la superficie de la tarjeta. Las marcas blancas o palidas (GitHub, MCP, OpenAI,
   Grok, Bun, Tauri, Prettier, Linux) llevan un filtro de oscurecido **solo en el tema
   claro**, para que no desaparezcan sobre blanco. En oscuro se ven tal cual.

Los iconos grandes de las tarjetas de proyecto son marcas completas y siguen sin ficha.
**QuickModel** se redondea en un derivado raster (`quickmodel-rounded.png`, esquinas
recortadas con alpha) porque GitHub borra el `style` que hacia el redondeado.

### Los botones del README

GitHub borra todo `style` y todo `<style>` del README, y el lector puede tener el tema claro o
el oscuro. Un enlace suelto siempre sale morado y no se puede convertir en boton desde el
markdown. La salida es una **imagen que lleva su propio contraste**: una ficha redondeada con
fondo fijo, el icono dentro y la etiqueta al lado.

`scripts/make-buttons.py` los genera en `assets/btn/`. Cubren:

- **Repositorios** (con el nombre del proyecto, no la palabra "Repository"), releases, docs,
  live, npm, LinkedIn, Docker Hub y el portfolio (con el logo de Cartago dentro).
- **Tecnologias** (`tech-*`): la misma ficha con el color de cada marca, para el Core stack.
- **Imagenes Docker** (`img-*`): la misma ficha con el nombre de la imagen.
- Los contadores de pulls de shields.io se recolorean a la paleta de la ficha
  (`labelColor=0e1a2b&color=2b4786`, `for-the-badge`) para que convivan con los botones.

La etiqueta lleva el **nombre del proyecto**. El ancho se calcula caractero a caractero
(`text_width`) con un 22% de holgura, porque la fuente del lector puede ser Segoe UI,
Helvetica o Arial, mas anchas que Inter, y recortaban las etiquetas largas.

**Alineacion:** los botones van en una fila `<tr>` propia, debajo de la fila de contenido. Si
van dentro de la misma celda que el texto, cada celda acaba a una altura distinta y los enlaces
no cuadran. Con la fila aparte, las tres celdas empiezan los botones a la misma altura.

**Cache del proxy:** GitHub sirve las imagenes del README a traves de un proxy que cachea por
URL completa y **ignora el `?v=2`**. Cuando se cambia un boton ya publicado, hay que renombrar
el fichero; cambiar el contenido o la query no basta. Por eso `repo-tanit.svg` paso a
`tanit.svg`. Para los cambios de ancho se uso `?v=3` en todas las referencias, que al ser una
URL nueva si fuerza la recarga.

### El logo de Cartago en el README

El logo entregado (`assets/cartago.svg`) preside el README: va dentro del `<h1>`, encima del
nombre, enlazado al portfolio. Para el boton pequeno se rasteriza a 128 px
(`scripts/make-cartago-thumb.py` → `cartago-128.png`, ~10 KB) porque el SVG original pesa
290 KB y a 15 px ese detalle no se ve.

## Trabajo profesional: donde va y donde no

Decision acordada con Mario:

- **El trabajo de empresa NO va al README de GitHub.** El README del perfil es solo trabajo
  independiente, verificable y clonable.
- **El trabajo de empresa SI va al portafolio**, en una seccion propia (`#pro`), porque es lo
  que sirve para una oferta o una subida de sueldo: demuestra impacto real.
- **LinkedIn** lleva la trayectoria completa con el nombre del employer.

La seccion del portafolio se redacta en modo «sector + escala + que construi», sin nombres de
cliente, sin cifras de negocio del employer y sin capturas. Los proyectos que estan en
`_projects/Beateam` se describen por su funcion: logistica de almacen, control de asistencia,
firma de recepcion, pantallas de almacen, proyectos y candidatos, ERP de servicios y minijuegos
para quioscos. Los commits de cada repositorio llevan la firma de Mario, asi que la evidencia
es real aunque el codigo no se publique.

Los datos que se usan salen de medir el repositorio, no de una estimacion: el numero de commits
del autor, el rango de fechas y el stack del `package.json`.

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

- La ficha de marca del encabezado es ahora el globo de `assets/cartago.svg` y el favicon es el
  mismo fichero.
- Las tarjetas de proyecto ponen el icono **encima** del titulo, para que el icono pertenezca al
  producto y no flote a la izquierda del texto.
- Los enlaces a GitHub, LinkedIn, npm y Docker Hub estan como enlaces con icono SVG.
- El bloque de contacto es una tarjeta coral, para que el final de la pagina tenga peso.
- Se anadieron los enlaces reales a los productos que funcionan: la app de Print CV y la
  documentacion de QuickModel.

### El banner

Decisiones de Mario, que se aplican tal cual:

1. **La imagen no se toca.** Ni recortes, ni Glow, ni recoloreado, ni `mix-blend-mode` sobre el
   fichero. `assets/cartago-banner.png` entra en el repositorio tal cual lo entrega.
2. **Va encima de "En una linea"**, no detras de la pagina: un bloque `.hero__aside` con la
   imagen por encima del panel de datos.
3. **Se funde con el fondo, sin forma propia.** En oscuro, `mix-blend-mode: screen` levanta el
   navy del arte y deja solo la marca iluminada; una mascara ovalada suave la disuelve en la
   pagina. En claro, compuesto normal a opacidad .32 con una mascara mas cerrada: una estampa
   tenue sobre el papel, sin rectangulo y con el wordmark legible. Nada de elipses apretadas —
   se leian como un huevo. Sin borde, sin sombra, en los dos temas.
4. **No esta en el fondo del encabezado ni del hero.** Se elimino la capa `.site-header::before`
   que lo repetia detras de la navegacion, y tambien la del `.hero` en tema claro. La imagen
   solo vive en el `.hero__aside`.
5. **Los iconos pequenos no llevan `loading="lazy"`.** Son SVG de menos de un kilobyte y el
   navegador integrado no los cargaba hasta hacer scroll sobre ellos. Cargan con la pagina.

### Interaccion

- La **barra de acento** de las tarjetas (pillars y projects) vive **dentro** del padding
  (`left: var(--s5); top: var(--s3)`), con radio propio: pertenece a la tarjeta redondeada,
  no corre por encima del borde. En reposo es corta y tenue; en hover crece hasta el ancho
  interior con transicion.
- Tarjetas, pills, botones e iconos tienen transiciones de ~.2s y un estado `:active`
  (escala .96–.99) que reconoce la pulsacion.
- Los **chips de tecnologia** de las tarjetas profesionales van al final del cuerpo
  (`margin-top: auto` dentro de un `project__body` flex), asi todas las tarjetas de una fila
  los muestran a la misma altura.
- `:focus-visible` con outline de 2px y offset 3px en todo lo interactivo.

### Revision UX externa (aplicada)

Una revision externa del portafolio señalo varios puntos; se aplicaron por orden de impacto:

1. **Navegacion movil.** `.site-nav` se ocultaba en ≤760px sin sustituto. Ahora hay un boton
   de menu (44×44) que abre un panel con todas las secciones y una accion **Contactar**
   visible. Se cierra con Escape o al navegar. Ojo: `.mobile-nav[hidden] { display: none }`
   es necesario porque el `display: grid` de la clase pisa el atributo `hidden`.
2. **CTAs de conversion.** El hero tenia "Ver el trabajo" y "Que hago" (explorar). Ahora:
   **Ver proyectos** (primario), **Contactar** y **Ver CV ↗** (enlaza a print-cv).
3. **Contraste AA.** El boton primario `#4d8dff` con blanco daba 3.2:1. Se oscurecio a
   `#2b66d9` (5.2:1). `--text-dim` subio en los dos temas (`#7a8db8` oscuro, `#5a6c8c` claro).
   La microtipografia paso de ~11px a 12px (.75rem). Los iconos del header y los toggles
   tienen superficie tactil de 44px.
4. **Casos de estudio.** Cinco trabajos profesionales llevan ahora **El reto** y **Mi
   contribucion**, con una **pantalla recreada** (mockups de divs con datos ficticios: PDA,
   movil con fichaje, canvas de firma, TV de almacen, quiosco de juegos). Nada de material
   del cliente; la forma del problema si se ve. Las tarjetas de caso ocupan dos columnas.
5. **Accesibilidad.** Los botones de tema (sol/luna) llevan `aria-label` descriptivo. El
   reveal ya tenia fallback sin IntersectionObserver.

Pendiente de la misma revision (no aplicado, requiere decision de Mario): reducir el volumen
inicial de tarjetas, y SEO bilingue con URLs diferenciadas por idioma.

### Idiomas

Cada texto visible lleva su par `(es, en)` y se emite con `i18n()`. La auditoria con el
navegador (buscar nodos de texto fuera de `[data-lang]` y spans del idioma equivocado
visibles) destapo tres fugas que ya estan corregidas: los **titulos de las tarjetas
profesionales** salian siempre en ingles, las **notas de evidencia** solo en español, y el
**skip-link** estaba fijado en ingles. Los valores del panel "En una linea" tambien son
bilingues ahora.

### Tema claro y oscuro en el README

GitHub no deja aplicar CSS al README, pero si respeta `<picture>` con
`media="(prefers-color-scheme: light)"`. Cada boton tiene su variante clara en
`assets/btn/light/` (ficha `#f2f5fb`, borde `#bfcee6`, etiqueta `#12233f`; las marcas blancas
pasan a su version oscura — GitHub negro, como en github.com). El README sirve la variante
correcta por tema con `<picture><source …><img …></picture>`.

Las **graficas de actividad** se guardan en el repositorio (`assets/activity/`), en los dos
temas, con esquinas redondeadas (12 px) y la paleta de la ficha. `scripts/refresh-activity.py`
las descarga y **hornea las animaciones de entrada a su estado final** (opacity 1, font-size
final, sin keyframes): dentro de un `<img>` algunos renderizadores no ejecutan la animacion y
la grafica se veia en blanco. Un workflow semanal (`refresh-activity.yml`, lunes 06:00 UTC)
las refresca y solo hace commit si cambiaron.

KPI añadido: **Most Used Languages** (top-langs, layout compact), con la misma ficha y radios
que el resto.

### Correo

`cv2mario@gmail.com` esta en la tarjeta de contacto (con icono de sobre) y en el footer del
portafolio, como enlace `mailto:`. En el README de GitHub no hace falta: ya sale en la barra
lateral del perfil.

El sitio sigue sin dependencias: se publica desde `main` tal cual en GitHub Pages.

## Redaccion de los proyectos

Los textos de cada proyecto dicen **que es el repositorio**, no para que sirve en general. Y no
anuncian lo que no esta terminado:

- La tarjeta de fabricacion de mods es **generica** —herramientas y contenido para modificar
  juegos: formatos binarios, localizacion y automatizacion— sin nombrar juegos ni campañas
  concretas, porque esos proyectos siguen en desarrollo.
- La tarjeta del portfolio **no dice "Angular 22 zoneless"**. Dice lo que hay: una pagina estatica
  generada desde un script, en dos idiomas y con el tema del sistema, con una aplicacion Angular
  con render en servidor detras.
- La ficha de Keyer se queda con lo suyo —cifrar credenciales desde la terminal— y no absorbe la
  de Steam Keys, que es otra cosa: un gestor local de claves de escritorio, en Tauri y SQLite.
- **DelendAI no es un «runtime MCP».** Es un servidor MCP con 62 plugins aisladas, una CLI,
  nueve presets y un ciclo de propuesta a release con 18 puertas de CI. La descripcion dice eso.
- **La seccion de evidencia lleva datos que aportan valor**: 89 repositorios (68 publicos, 21
  privados), 26 activos, 22.638 commits en los publicos activos, cinco anos publicando desde
  octubre de 2021. El numero de paquetes que nadie usa no dice nada; el de repositorios y el de
  anos si.
- **Los enlaces llevan el nombre del proyecto**, no la palabra «Repositorio». En el portafolio
  son pills con icono; en el README son botones con el nombre dentro.

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
5. ~~**Logo y banner definitivos del portfolio.**~~ Resuelto: la marca entregada (el globo) y el
   banner estan ya en el repositorio del perfil y en el sitio. El README del perfil usa
   `banner-03-neon.png` como cabecera y el sitio usa `cartago-banner.png` sobre "En una linea".

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
