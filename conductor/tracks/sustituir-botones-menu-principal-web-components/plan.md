# Plan de Implementación: Sustituir botones del menú principal por Web Components

## Tarea

Reemplazar los botones HTML estándar en el menú principal de `index.html` por instancias del Web Component `app-button-blue`, asegurando que la funcionalidad JavaScript existente se mantenga.

## Archivos a Modificar

*   `interface/index.html`
*   `interface/js/scripts.js`

## Pasos

1.  **Modificar `interface/index.html`**:
    *   Para cada botón `button` dentro de `div class="menu-options"`, reemplazarlo con su correspondiente `<app-button-blue>`.
    *   Transferir los atributos `id` y `data-action` al Custom Element `app-button-blue`.
    *   El texto del botón original será el contenido del Custom Element.

    **Ejemplo de cambio:**
    De:
    ```html
    <button id="btnNuevoReporte" data-action="nuevo">Nuevo Reporte</button>
    ```
    A:
    ```html
    <app-button-blue id="btnNuevoReporte" data-action="nuevo">Nuevo Reporte</app-button-blue>
    ```
    Hacer esto para los 5 botones.

2.  **Modificar `interface/js/scripts.js`**:
    *   Como el Web Component `app-button-blue` despacha un evento `click` que burbujea y se compone (`bubbles: true, composed: true`), los `eventListeners` existentes que están adjuntos a los botones por su `id` (por ejemplo, `btnNuevoReporte.addEventListener("click", ...)`) deberían seguir funcionando sin cambios.
    *   Sin embargo, es crucial verificar este comportamiento y, si es necesario, ajustar la forma en que se obtienen las referencias a los elementos o se adjuntan los `eventListeners`.

3.  **Actualizar la versión del script de JavaScript en `index.html`**: Para forzar la recarga del navegador y asegurar que los cambios se apliquen.

## Verificación

*   Recargar la página de la aplicación en el navegador.
*   Verificar visualmente que los botones del menú principal se renderizan correctamente con el estilo azul de `app-button-blue`.
*   Hacer clic en cada botón del menú principal y verificar que la funcionalidad asociada (abrir formularios, listar reportes) sigue operando como se espera.
*   Abrir la consola del navegador y verificar que no hay errores de JavaScript.

Comenzaré con el Paso 1: Modificar `interface/index.html`. Para ello, primero leeré el archivo.
