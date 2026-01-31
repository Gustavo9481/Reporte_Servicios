# Especificación: Crear Web Components para botones de colores

## Objetivo

Crear tres Web Components reutilizables para botones, cada uno con un color predefinido (azul, rojo, verde), utilizando los estilos definidos previamente en las variables CSS globales. Estos componentes encapsularán la lógica y el estilo de los botones, facilitando su uso y mantenimiento en la interfaz.

## Requisitos

1.  **Componentes a crear**:
    *   `app-button-blue`: Un botón con estilo azul.
    *   `app-button-red`: Un botón con estilo rojo.
    *   `app-button-green`: Un botón con estilo verde.
2.  **Ubicación**: Cada componente debe tener su propio archivo JavaScript y CSS (si es necesario) dentro de `interface/components/` en una subcarpeta específica para el componente. Por ejemplo:
    *   `interface/components/app-button-blue/app-button-blue.js`
    *   `interface/components/app-button-red/app-button-red.js`
    *   `interface/components/app-button-green/app-button-green.js`
3.  **Tecnología**: Los componentes deben ser creados utilizando la API estándar de Web Components (Custom Elements, Shadow DOM).
4.  **Estilo**:
    *   Los componentes deben utilizar las variables CSS globales (`--blue-color`, `--red-color`, `--green-color`, `--white-color`) definidas en `interface/css/styles.css` para sus colores de fondo y texto.
    *   Deben heredar o replicar un estilo base consistente (padding, border, border-radius, font-size, cursor, transición de hover).
    *   Cada botón debe tener un efecto `hover` que oscurezca ligeramente su color de fondo, similar al comportamiento actual de los botones en la aplicación.
    *   Los estilos deben estar encapsulados dentro del Shadow DOM de cada componente.
5.  **Contenido (Slot)**: Cada componente debe aceptar contenido dinámico (texto o HTML) a través de un `<slot>`.
6.  **Funcionalidad**:
    *   Los componentes deben comportarse como un botón HTML estándar, emitiendo un evento `click` cuando se presionan.
7.  **Accesibilidad**: Deben ser accesibles y semánticamente correctos (utilizar la etiqueta `<button>` internamente).

## Archivos Afectados (Creación)

*   `interface/components/app-button-blue/app-button-blue.js`
*   `interface/components/app-button-red/app-button-red.js`
*   `interface/components/app-button-green/app-button-green.js`

## Criterios de Aceptación

*   Existen los tres archivos JavaScript para los Web Components en sus ubicaciones correctas.
*   Cada componente se registra como un Custom Element (`customElements.define`).
*   Cada componente renderiza un `<button>` interno que muestra el contenido pasado a través de un `<slot>`.
*   Cada botón tiene el color de fondo y texto correcto según su tipo (azul, rojo, verde), utilizando las variables CSS globales.
*   Los botones tienen un efecto `hover` que cambia su color de fondo.
*   Al hacer clic en un botón, se emite un evento `click` estándar que puede ser capturado por un listener externo.
*   Los estilos de los componentes están encapsulados y no interfieren con el resto de la página.
*   La implementación sigue las mejores prácticas de Web Components.
