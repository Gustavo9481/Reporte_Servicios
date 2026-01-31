# Plan de Implementación: Corregir tamaño del botón "Volver a la lista" y uniformar botones en vistas/formularios

## Tarea

Ajustar los estilos de los contenedores `div.form-actions` en las funciones JavaScript que generan el HTML (`renderNewReportForm`, `renderEditReportForm`, `showReportDetails`) para que los botones Web Components dentro de ellos tengan un ancho consistente y un espaciado adecuado.

## Archivos a Modificar

*   `interface/js/scripts.js`
*   `interface/index.html` (para incrementar la versión del script principal)

## Pasos

### 1. Modificar `interface/js/scripts.js`

**A. Función `renderNewReportForm` (Crear Nuevo Reporte)**

1.  Localizar el `div class="form-actions"`:
    *   **Old**: `<div class="form-actions">`
    *   **New**: `<div class="form-actions" style="display: flex; gap: 10px; justify-content: flex-end;">`
    *   **Justificación**: Añadir `display: flex` para organizar los botones, `gap` para el espaciado entre ellos y `justify-content: flex-end` para alinearlos a la derecha, como era el comportamiento anterior.

**B. Función `renderEditReportForm` (Editar Reporte)**

1.  Localizar el `div class="form-actions"`:
    *   **Old**: `<div class="form-actions">`
    *   **New**: `<div class="form-actions" style="display: flex; gap: 10px; justify-content: flex-end;">`
    *   **Justificación**: Mismas razones que para `renderNewReportForm`.

**C. Función `showReportDetails` (Detalles del Reporte)**

1.  Localizar el `div class="form-actions"`:
    *   **Old**: `<div class="form-actions" style="text-align: right; margin-top: 20px;">`
    *   **New**: `<div class="form-actions" style="margin-top: 20px; display: flex; gap: 10px; justify-content: flex-end;">`
    *   **Justificación**: Reemplazar `text-align: right` por `display: flex` con `justify-content: flex-end` para una alineación más moderna y consistente con los otros formularios, y mantener el `margin-top`.

### 2. Modificar `interface/index.html`

*   Incrementar la versión del script principal (`scripts.js`) para forzar la recarga del navegador.

## Verificación

*   Recargar la aplicación en el navegador.
*   Navegar a las páginas de "Crear Nuevo Reporte", "Editar Reporte" y "Detalles del Reporte".
*   Verificar visualmente que los botones dentro de los `div.form-actions` (incluyendo "Volver a la lista" y "Generar PDF" en Detalles) tienen un ancho y espaciado consistente, y están alineados a la derecha.
*   Verificar que la funcionalidad de todos los botones se mantiene.
*   Abrir la consola del navegador y verificar que no hay errores de JavaScript.

Comenzaré con el Paso 1.A: Modificar `interface/js/scripts.js` para `renderNewReportForm`. Para ello, primero leeré el archivo.
