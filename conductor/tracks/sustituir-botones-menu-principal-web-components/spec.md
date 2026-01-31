# Especificación: Sustituir botones del menú principal por Web Components

## Objetivo

Migrar los botones estáticos del menú principal en `interface/index.html` a `app-button-blue` Web Components, manteniendo la funcionalidad actual y la semántica.

## Requisitos

1.  **Botones a sustituir**: Todos los botones dentro de `div class="menu-options"` en `interface/index.html`.
    *   `id="btnNuevoReporte"`
    *   `id="btnConsultarReporte"`
    *   `id="btnConsultarPlaca"`
    *   `id="btnConsultarCliente"`
    *   `id="btnListaReportes"`
2.  **Componente a usar**: `app-button-blue`.
3.  **Mantener `id` y `data-action`**: Los `id` y `data-action` originales de los botones deben ser transferidos al Custom Element (`app-button-blue`) para asegurar que el JavaScript existente (`scripts.js`) pueda seguir referenciándolos y gestionando sus eventos.
4.  **Mantener texto**: El texto visible de cada botón debe ser el contenido del `slot` del Web Component.
5.  **Funcionalidad**: Los `eventListeners` definidos en `interface/js/scripts.js` deben seguir funcionando correctamente después de la sustitución. Esto implica que el `scripts.js` debe seguir pudiendo obtener las referencias a los botones por su `id`.

## Archivos Afectados

*   `interface/index.html`
*   `interface/js/scripts.js`

## Criterios de Aceptación

*   La sección `div class="menu-options"` en `index.html` contiene instancias de `app-button-blue`.
*   Cada `app-button-blue` tiene el `id` y `data-action` correctos.
*   El texto de cada botón se muestra correctamente.
*   Al hacer clic en los botones del menú, la funcionalidad esperada se ejecuta (ej. mostrar el formulario de nuevo reporte, listar reportes).
*   Los estilos de los botones `app-button-blue` son consistentes con el diseño de la aplicación.
*   No hay errores en la consola del navegador.
