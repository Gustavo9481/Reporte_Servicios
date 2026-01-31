# Plan de Implementación: Agregar botón "Cancelar" al formulario de Nuevo Reporte

## Tarea

Agregar un botón "Cancelar" al formulario de "Crear Nuevo Reporte" en la interfaz, con estilo rojo y funcionalidad para redirigir a la pantalla principal.

## Archivos a Modificar

*   `interface/js/scripts.js`
*   `interface/css/styles.css`

## Pasos

1.  **Modificar `interface/js/scripts.js`:**
    *   Dentro de la función `renderNewReportForm`, localizar el bloque `div class="form-actions"` al final del formulario.
    *   **Agregar el botón "Cancelar"**: Insertar un nuevo botón `<button type="button" id="btnCancelarNuevoReporte">Cancelar</button>` justo antes del botón `Guardar Reporte`.
    *   **Adjuntar `eventListener` al botón "Cancelar"**:
        *   Obtener una referencia al nuevo botón por su ID (`btnCancelarNuevoReporte`).
        *   Añadir un `eventListener` para el evento `click`.
        *   Dentro del `eventListener`, llamar a `showContent("")` para limpiar el `contentArea` y luego simular un clic en el botón `btnListaReportes.click()` para volver a la pantalla principal (lista de reportes).

2.  **Modificar `interface/css/styles.css`:**
    *   Buscar la clase `.btn-generar-pdf` o `.btn-remove` para ver cómo se aplica el color rojo (`#c1121f`).
    *   Añadir una nueva clase CSS, por ejemplo `.btn-cancel` o reutilizar `.btn-remove`, para darle el estilo de color de fondo rojo al nuevo botón "Cancelar".
        *   Si se crea una nueva clase, definir `background-color: #c1121f;` y `&:hover` con un color más oscuro (ej. `#9a0e19`).

3.  **Verificación**:
    *   Recargar la página.
    *   Hacer clic en "Nuevo Reporte".
    *   Verificar que el botón "Cancelar" aparece a la izquierda de "Guardar Reporte" y tiene el color rojo deseado.
    *   Hacer clic en el botón "Cancelar" y verificar que el formulario desaparece y se muestra la lista de reportes (o el menú principal si no hay reportes).
    *   Verificar que la funcionalidad de "Guardar Reporte" sigue funcionando correctamente.

## Reutilización de Estilos existentes:

El archivo `styles.css` ya cuenta con la clase `.btn-remove` que utiliza el color rojo `#c1121f` y un efecto hover. Esta clase puede ser reutilizada para el botón "Cancelar", de esta manera no será necesario crear una clase específica.

Este plan detalla los cambios necesarios para implementar la funcionalidad solicitada. Procederé a ejecutar el paso 1.1.
