# Especificación: Corregir tamaño del botón "Volver a la lista" y uniformar botones en vistas/formularios

## Objetivo

Ajustar el tamaño y la alineación de los botones dentro de los `div.form-actions` en las vistas de "Detalles del Reporte" y "Editar Reporte", así como en el formulario de "Crear Nuevo Reporte", para que sean consistentes y ocupen el ancho esperado. Específicamente, se busca corregir el tamaño del botón "Volver a la lista" en la pantalla de detalles del reporte.

## Requisitos

1.  **Uniformidad de Botones**: Los botones dentro de los `div.form-actions` deben tener un comportamiento de ancho y espaciado consistente, similar al `div.menu-options` que utiliza `display: flex` y `gap`.
2.  **Corrección de "Volver a la lista"**: El botón "Volver a la lista" en la vista de "Detalles del Reporte" debe adoptar el ancho correcto (al menos `min-width: 140px`) y no mostrarse encogido.
3.  **No alterar funcionalidad**: La funcionalidad de cada botón debe mantenerse intacta.
4.  **No introducir errores**: No deben aparecer nuevos errores en la consola del navegador.

## Archivos Afectados

*   `interface/js/scripts.js`
*   `interface/index.html` (para incrementar la versión del script principal)

## Análisis Detallado

El problema actual con el botón "Volver a la lista" y otros botones en los `form-actions` de las vistas de detalles y edición probablemente se debe a que el contenedor (`div.form-actions`) no está utilizando `display: flex` para gestionar el espaciado y la distribución de sus elementos internos de manera uniforme. Los Web Components de botones tienen un `min-width: 140px` interno, pero si su contenedor no los organiza explícitamente, su `display: inline-block` puede hacer que se agrupen de forma compacta.

Para replicar el comportamiento deseado, aplicaremos `display: flex` y `gap` al `div.form-actions` directamente en las cadenas de HTML generadas por JavaScript.

## Criterios de Aceptación

*   El botón "Volver a la lista" en la vista de "Detalles del Reporte" tiene el tamaño correcto.
*   Todos los botones dentro de los `div.form-actions` en las páginas de "Crear Nuevo Reporte", "Editar Reporte" y "Detalles del Reporte" se ven uniformes en tamaño y espaciado.
*   La funcionalidad de todos los botones se mantiene.
*   No hay errores en la consola del navegador.
