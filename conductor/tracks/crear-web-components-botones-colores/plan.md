# Plan de Implementación: Crear Web Components para botones de colores

## Tarea

Crear los Web Components `app-button-blue`, `app-button-red` y `app-button-green` con estilos y funcionalidades específicas, utilizando las variables CSS globales previamente definidas.

## Archivos a Modificar (Crear)

*   `interface/components/app-button-blue/app-button-blue.js`
*   `interface/components/app-button-red/app-button-red.js`
*   `interface/components/app-button-green/app-button-green.js`
*   `interface/components/app-button-blue/app-button-blue.css` (Para encapsular los estilos específicos si es necesario)
*   `interface/components/app-button-red/app-button-red.css`
*   `interface/components/app-button-green/app-button-green.css`

## Pasos

1.  **Crear directorios para cada componente**:
    *   `mkdir -p interface/components/app-button-blue`
    *   `mkdir -p interface/components/app-button-red`
    *   `mkdir -p interface/components/app-button-green`

2.  **Crear el archivo `app-button-blue/app-button-blue.js`**:
    *   Definir una clase `AppButtonBlue` que extienda `HTMLElement`.
    *   Implementar `constructor()`:
        *   Crear un `shadowRoot`.
        *   Crear un `<style>` dentro del `shadowRoot` para los estilos específicos del botón.
        *   Los estilos deben usar las variables CSS globales (`var(--blue-color)`, `var(--white-color)`).
        *   Incluir estilos base (padding, border, border-radius, cursor, font-size, transition).
        *   Definir un estilo `:hover` que use un color azul más oscuro (ej. `var(--darker-blue)` si se definiera una variable específica, o un `darken` programático en CSS si fuera posible). Por ahora, usaremos `#3a56d4` directamente o inferiremos de los estilos existentes.
        *   Crear un elemento `<button>` dentro del `shadowRoot`.
        *   Añadir un `<slot>` dentro del `<button>` para el contenido.
        *   Añadir un `eventListener` al botón interno para despachar un evento `click` al host del componente.
    *   Registrar el Custom Element: `customElements.define('app-button-blue', AppButtonBlue)`.

3.  **Crear el archivo `app-button-red/app-button-red.js`**:
    *   Similar al `app-button-blue.js`, pero con estilos para el color rojo (`var(--red-color)` para fondo y un `darken` para `:hover`, o `#9a0e19` directamente).

4.  **Crear el archivo `app-button-green/app-button-green.js`**:
    *   Similar al `app-button-blue.js`, pero con estilos para el color verde (`var(--green-color)` para fondo y un `darken` para `:hover`, o `#217d72` directamente).

5.  **Actualizar `interface/index.html`**:
    *   Incluir los nuevos archivos JavaScript de los Web Components en el `<body>` para que se definan. Se puede hacer con `<script type="module" src="..."></script>`.
    *   Incrementar la versión del script de JavaScript en el `index.html` para forzar la recarga del navegador.

## Reutilización de estilos y el problema de `:host` en Shadow DOM

Considerando que estamos usando Shadow DOM, los estilos globales del `styles.css` no afectarán directamente a los elementos dentro del `shadowRoot`. Por lo tanto, tendremos que replicar los estilos base de los botones dentro del `<style>` de cada Shadow DOM, utilizando las variables CSS globales.

Para los colores más oscuros en el `hover`, si no hemos definido variables `--darker-blue`, etc., podemos inferir de los colores existentes en `styles.css` o simplemente definir un color un poco más oscuro. Basándome en `styles.css`:
*   Para azul: `var(--blue-color)` (`#4361ee`) y hover `#3a56d4`.
*   Para rojo: `var(--red-color)` (`#c1121f`) y hover `#9a0e19`.
*   Para verde: `var(--green-color)` (`#2a9d8f`) y hover `#217d72`.

Comenzaré con el Paso 1: Crear los directorios para cada componente.
