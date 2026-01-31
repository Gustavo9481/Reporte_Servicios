# Especificación: Agregar botón "Cancelar" al formulario de Nuevo Reporte

## Objetivo

Agregar un botón "Cancelar" a la interfaz de "Crear Nuevo Reporte". Este botón permitirá al usuario descartar la creación de un nuevo reporte y volver a la pantalla principal, mejorando la usabilidad.

## Requisitos

1.  **Ubicación**: El botón "Cancelar" debe estar a la izquierda del botón "Guardar Reporte" dentro de la sección `form-actions`.
2.  **Etiqueta**: El texto del botón debe ser "Cancelar".
3.  **Estilo**:
    *   Debe tener un color de fondo rojo, respetando la paleta de colores del proyecto (`#c1121f` o similar a los botones de eliminar/generar PDF).
    *   Debe seguir los estilos generales de los botones existentes en la aplicación (`padding`, `border-radius`, `font-size`, etc.).
4.  **Funcionalidad**: Al hacer clic en el botón "Cancelar", el formulario de "Crear Nuevo Reporte" debe desaparecer y la interfaz debe volver a mostrar la pantalla principal, que es el menú de opciones. Esto se puede lograr simulando un clic en el botón "Lista de Reportes" o similar para restablecer la vista.

## Archivos Afectados

*   `interface/js/scripts.js`:
    *   Modificación de la función `renderNewReportForm` para incluir el nuevo botón "Cancelar" en el HTML generado.
    *   Adición de un `eventListener` al botón "Cancelar" para manejar su lógica de navegación.
*   `interface/css/styles.css`:
    *   Posible adición de una nueva clase CSS para el estilo específico del botón rojo "Cancelar", si los estilos existentes no son adecuados. Si existe una clase de color rojo para botones (e.g., `btn-remove` o `btn-generar-pdf`), se reutilizará.

## Criterios de Aceptación

*   El botón "Cancelar" es visible en el formulario de "Crear Nuevo Reporte".
*   El botón tiene el texto "Cancelar" y un estilo visual que lo diferencia claramente (color rojo).
*   Al hacer clic en "Cancelar", el formulario se cierra y la aplicación vuelve a la pantalla inicial del menú (lista de opciones).
*   No hay errores en la consola del navegador al interactuar con el botón.
*   La funcionalidad de "Guardar Reporte" sigue operando correctamente.
