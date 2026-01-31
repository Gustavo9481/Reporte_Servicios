# Especificación: Sustituir botones en formularios y vistas de detalles por Web Components

## Objetivo

Reemplazar los botones HTML estándar en las páginas de "Crear Nuevo Reporte", "Editar Reporte" y "Detalles del Reporte" por sus equivalentes Web Components (`app-button-blue`, `app-button-red`, `app-button-green`), manteniendo la funcionalidad y los estilos visuales.

## Requisitos

### General para todos los reemplazos de botones:

*   Se utilizará el Web Component (`app-button-blue`, `app-button-red`, `app-button-green`) que coincida con el tamaño y el color actual del botón HTML estándar.
*   Los `id` de los botones originales deben ser transferidos al Custom Element para mantener la referencia en `scripts.js`.
*   El texto visible del botón original será el contenido (`slot`) del Web Component.
*   La funcionalidad (`eventListeners`) asociada a los botones debe permanecer intacta.
*   No se deben introducir errores en la consola del navegador.

### Página "Crear Nuevo Reporte" (`renderNewReportForm` en `scripts.js`)

1.  **Botón "Cancelar"**:
    *   Sustituir el `<button id="btnCancelarNuevoReporte" class="btn-remove">Cancelar</button>` por `<app-button-red id="btnCancelarNuevoReporte">Cancelar</app-button-red>`.
2.  **Botón "Guardar Reporte"**:
    *   Sustituir el `<button type="submit">Guardar Reporte</button>` por `<app-button-green type="submit">Guardar Reporte</app-button-green>`.
3.  **Botones "+ Añadir Servicio" y "+ Añadir Repuesto"**:
    *   Sustituir los `<button type="button" id="btnAddServicio" class="btn-add">+ Añadir Servicio</button>` y `<button type="button" id="btnAddRepuesto" class="btn-add">+ Añadir Repuesto</button>` por `<app-button-blue id="btnAddServicio">+ Añadir Servicio</app-button-blue>` y `<app-button-blue id="btnAddRepuesto">+ Añadir Repuesto</app-button-blue>` respectivamente.
4.  **Botones "X" (eliminar servicio/repuesto)**:
    *   Sustituir el `<button type="button" class="btn-remove">X</button>` generado dinámicamente por `<app-button-red class="btn-remove">X</app-button-red>`.

### Página "Editar Reporte" (`renderEditReportForm` en `scripts.js`)

1.  **Botón "Cancelar"**:
    *   Sustituir el `<button type="button" id="btnCancelarEdicion" class="btn-remove">Cancelar</button>` por `<app-button-red id="btnCancelarEdicion">Cancelar</app-button-red>`.
2.  **Botón "Actualizar Reporte"**:
    *   Sustituir el `<button type="submit">Actualizar Reporte</button>` por `<app-button-green type="submit">Actualizar Reporte</app-button-green>`.
3.  **Botones "+ Añadir Servicio" y "+ Añadir Repuesto"**:
    *   Sustituir los `<button type="button" id="btnAddServicio" class="btn-add">+ Añadir Servicio</button>` y `<button type="button" id="btnAddRepuesto" class="btn-add">+ Añadir Repuesto</app-button-blue>` por `<app-button-blue id="btnAddServicio">+ Añadir Servicio</app-button-blue>` y `<app-button-blue id="btnAddRepuesto">+ Añadir Repuesto</app-button-blue>` respectivamente.
4.  **Botones "X" (eliminar servicio/repuesto)**:
    *   Sustituir el `<button type="button" class="btn-remove">X</button>` generado dinámicamente por `<app-button-red class="btn-remove">X</app-button-red>`.

### Página "Detalles del Reporte" (`showReportDetails` en `scripts.js`)

1.  **Botón "Volver a la lista"**:
    *   Sustituir el `<button id="btnVolverLista">Volver a la lista</button>` por `<app-button-blue id="btnVolverLista">Volver a la lista</app-button-blue>`.
2.  **Botón "Editar Reporte"**:
    *   Sustituir el `<button id="btnEditarReporte" class="btn-editar">Editar Reporte</button>` por `<app-button-green id="btnEditarReporte">Editar Reporte</app-button-green>`.
3.  **Botón "Generar PDF"**:
    *   Sustituir `<a href="/reportes/${reporteId}/pdf" target="_blank" class="btn-generar-pdf">Generar PDF</a>` por `<app-button-red id="btnGenerarPDF">Generar PDF</app-button-red>`. La funcionalidad de descarga se replicará a través de un `eventListener`.

## Archivos Afectados

*   `interface/js/scripts.js`

## Criterios de Aceptación

*   Todos los botones especificados en las páginas de "Crear Nuevo Reporte", "Editar Reporte" y "Detalles del Reporte" son ahora Custom Elements de tipo `app-button-blue`, `app-button-red` o `app-button-green`.
*   La apariencia visual de los botones se mantiene (colores, padding, etc.).
*   La funcionalidad de cada botón se mantiene intacta.
*   No hay errores en la consola del navegador.
*   El botón "Generar PDF" ahora es un `app-button-red` y al hacer clic descarga el PDF.
