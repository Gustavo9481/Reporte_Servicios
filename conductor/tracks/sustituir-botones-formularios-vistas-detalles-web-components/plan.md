# Plan de Implementación: Sustituir botones en formularios y vistas de detalles por Web Components

## Tarea

Reemplazar los botones HTML estándar en las páginas "Crear Nuevo Reporte", "Editar Reporte" y "Detalles del Reporte" por sus equivalentes Web Components (`app-button-blue`, `app-button-red`, `app-button-green`), manteniendo la funcionalidad y los estilos visuales.

## Archivos a Modificar

*   `interface/js/scripts.js`
*   `interface/index.html` (para incrementar la versión del script principal)

## Pasos

### 1. Modificar `interface/js/scripts.js`

**A. Función `renderNewReportForm` (Crear Nuevo Reporte)**

1.  **Botón "Cancelar"**:
    *   **Old**: `<button type="button" id="btnCancelarNuevoReporte" class="btn-remove">Cancelar</button>`
    *   **New**: `<app-button-red id="btnCancelarNuevoReporte">Cancelar</app-button-red>`
    *   **Acción**: Reemplazar en la cadena `html`. El `eventListener` ya está adjunto al `id`, por lo que debería seguir funcionando.
2.  **Botón "Guardar Reporte"**:
    *   **Old**: `<button type="submit">Guardar Reporte</button>`
    *   **New**: `<app-button-green type="submit">Guardar Reporte</app-button-green>`
    *   **Acción**: Reemplazar en la cadena `html`. El `eventListener` del formulario `submit` lo capturará.
3.  **Botones "+ Añadir Servicio" y "+ Añadir Repuesto"**:
    *   **Old**: `<button type="button" id="btnAddServicio" class="btn-add">+ Añadir Servicio</button>`
    *   **New**: `<app-button-blue id="btnAddServicio">+ Añadir Servicio</app-button-blue>`
    *   **Old**: `<button type="button" id="btnAddRepuesto" class="btn-add">+ Añadir Repuesto</button>`
    *   **New**: `<app-button-blue id="btnAddRepuesto">+ Añadir Repuesto</app-button-blue>`
    *   **Acción**: Reemplazar en la cadena `html`. Los `eventListeners` ya están adjuntos al `id`.
4.  **Botones "X" (eliminar servicio/repuesto - dinámicos)**:
    *   **Old**: `<button type="button" class="btn-remove">X</button>`
    *   **New**: `<app-button-red class="btn-remove">X</app-button-red>`
    *   **Acción**: Modificar las plantillas de string que generan el `innerHTML` para `div.dynamic-item` en ambos `eventListeners` de `btnAddServicio` y `btnAddRepuesto`.

**B. Función `renderEditReportForm` (Editar Reporte)**

1.  **Botón "Cancelar"**:
    *   **Old**: `<button type="button" id="btnCancelarEdicion" class="btn-remove">Cancelar</button>`
    *   **New**: `<app-button-red id="btnCancelarEdicion">Cancelar</app-button-red>`
    *   **Acción**: Reemplazar en la cadena `html`. El `eventListener` ya está adjunto al `id`.
2.  **Botón "Actualizar Reporte"**:
    *   **Old**: `<button type="submit">Actualizar Reporte</button>`
    *   **New**: `<app-button-green type="submit">Actualizar Reporte</app-button-green>`
    *   **Acción**: Reemplazar en la cadena `html`. El `eventListener` del formulario `submit` lo capturará.
3.  **Botones "+ Añadir Servicio" y "+ Añadir Repuesto"**:
    *   **Old**: `<button type="button" id="btnAddServicio" class="btn-add">+ Añadir Servicio</button>`
    *   **New**: `<app-button-blue id="btnAddServicio">+ Añadir Servicio</app-button-blue>`
    *   **Old**: `<button type="button" id="btnAddRepuesto" class="btn-add">+ Añadir Repuesto</button>`
    *   **New**: `<app-button-blue id="btnAddRepuesto">+ Añadir Repuesto</app-button-blue>`
    *   **Acción**: Reemplazar en la cadena `html`. Los `eventListeners` ya están adjuntos al `id`.
4.  **Botones "X" (eliminar servicio/repuesto - dinámicos)**:
    *   **Old**: `<button type="button" class="btn-remove">X</button>`
    *   **New**: `<app-button-red class="btn-remove">X</app-button-red>`
    *   **Acción**: Modificar las plantillas de string que generan el `innerHTML` para `div.dynamic-item` en ambos bloques (inicial y `eventListeners` de `btnAddServicio` y `btnAddRepuesto`).

**C. Función `showReportDetails` (Detalles del Reporte)**

1.  **Botón "Volver a la lista"**:
    *   **Old**: `<button id="btnVolverLista">Volver a la lista</button>`
    *   **New**: `<app-button-blue id="btnVolverLista">Volver a la lista</app-button-blue>`
    *   **Acción**: Reemplazar en la cadena `html`. El `eventListener` ya está adjunto al `id`.
2.  **Botón "Editar Reporte"**:
    *   **Old**: `<button id="btnEditarReporte" class="btn-editar">Editar Reporte</button>`
    *   **New**: `<app-button-green id="btnEditarReporte">Editar Reporte</app-button-green>`
    *   **Acción**: Reemplazar en la cadena `html`. El `eventListener` ya está adjunto al `id`.
3.  **Botón "Generar PDF"**:
    *   **Old**: `<a href="/reportes/${reporteId}/pdf" target="_blank" class="btn-generar-pdf">Generar PDF</a>`
    *   **New**: `<app-button-red id="btnGenerarPDF">Generar PDF</app-button-red>`
    *   **Acción**: Reemplazar en la cadena `html`. El `target="_blank"` y `href` deberán ser manejados por un nuevo `eventListener` adjunto a `btnGenerarPDF` en `scripts.js`.

    *   **Nueva lógica para "Generar PDF"**:
        *   Dentro de `showReportDetails`, después de `showContent(html)`, añadir un `eventListener` al `document.getElementById("btnGenerarPDF")`.
        *   En el `eventListener`, al hacer click, obtener el `reporteId`.
        *   Construir la URL del PDF: `/reportes/${reporteId}/pdf`.
        *   Abrir una nueva ventana/pestaña con `window.open(pdfUrl, '_blank');`.

### 2. Modificar `interface/index.html`

*   Incrementar la versión del script principal (`scripts.js`) para forzar la recarga del navegador.

## Verificación

*   Recargar la aplicación en el navegador.
*   Navegar a cada una de las páginas ("Crear Nuevo Reporte", "Editar Reporte", "Detalles del Reporte").
*   Verificar visualmente que todos los botones han sido sustituidos por los Web Components correspondientes y mantienen su estilo.
*   Hacer clic en cada botón y verificar que su funcionalidad se mantiene intacta.
*   En el caso del botón "Generar PDF", verificar que al hacer clic se abre el PDF en una nueva pestaña.
*   Abrir la consola del navegador y verificar que no hay errores de JavaScript.

Comenzaré con la modificación de `interface/js/scripts.js`, sección A: `renderNewReportForm`. Para ello, primero leeré el archivo.
