# Especificación: Aplicar estilo rojo al botón "Cancelar" de Editar Reporte

## Objetivo

Uniformar el estilo del botón "Cancelar" en el formulario de edición de reportes para que coincida con la paleta de colores de la aplicación, específicamente utilizando el color rojo asociado a acciones de cancelación o eliminación, como se ha hecho con el botón de "Cancelar" en el formulario de creación de nuevos reportes.

## Requisitos

1.  **Ubicación**: El cambio se aplicará al botón "Cancelar" dentro del bloque `form-actions` de la función `renderEditReportForm` en `interface/js/scripts.js`.
2.  **Estilo**: El botón debe adoptar el color de fondo rojo definido por la variable `--red-color` o por la clase CSS `.btn-remove`.
3.  **Funcionalidad**: La funcionalidad actual del botón "Cancelar" (volver a la vista de detalles del reporte) debe mantenerse intacta.

## Archivos Afectados

*   `interface/js/scripts.js`

## Criterios de Aceptación

*   El botón "Cancelar" en el formulario de "Editar Reporte" es visible y tiene el color de fondo rojo.
*   Al hacer clic en el botón "Cancelar", el formulario de edición se cierra y se muestra la vista de detalles del reporte que se estaba editando.
*   No se introduce ningún otro cambio visual o funcional indeseado en la interfaz.
*   No hay errores en la consola del navegador.
