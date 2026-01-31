# Especificación: Ajustar ancho de Web Components de botones

## Objetivo

Garantizar que todos los Web Components de botones (`app-button-blue`, `app-button-red`, `app-button-green`) tengan un ancho uniforme y consistente con el diseño anterior de la interfaz, especialmente en los menús y formularios donde se utilizan.

## Requisitos

1.  **Ancho Consistente**: Los Custom Elements de botones deben tener un ancho que les permita alinearse y verse uniformes en la interfaz. El ancho original de los botones del menú principal era `min-width: 140px;` y `width: auto;`.
2.  **Aplicación de Estilo**: El estilo debe aplicarse a nivel del Custom Element o a su contenido (`button` interno) para afectar al componente en sí.
3.  **Mantener Flexibilidad**: El ancho no debe ser excesivamente restrictivo, permitiendo que el texto se ajuste y el botón crezca si es necesario (manteniendo `width: auto` pero con un `min-width`).
4.  **No afectar estilos internos**: Los estilos internos del Shadow DOM de cada Web Component (padding, color, etc.) deben permanecer inalterados.

## Análisis de Ancho Actual

Revisando `interface/css/styles.css`, la clase `.menu-options button` tenía:
```css
.menu-options button {
    padding: 8px 14px;
    font-size: 13px;
    min-width: 140px;
    width: auto;
}
```
Esto sugiere que un `min-width: 140px` es un buen punto de partida para los botones del menú. Para los botones dentro de formularios, el ancho se ajustaba automáticamente al `100%` del contenedor.

Considerando que los Web Components ahora reemplazan a estos botones, necesitamos aplicar los estilos a los Custom Elements directamente o a su Shadow DOM. El Shadow DOM encapsula los estilos, por lo que una opción es que los Web Components hereden o incorporen un `min-width` para su botón interno.

## Archivos Afectados

*   `interface/components/app-button-blue/app-button-blue.js`
*   `interface/components/app-button-red/app-button-red.js`
*   `interface/components/app-button-green/app-button-green.js`
*   `interface/css/styles.css` (para estilos que apliquen al Custom Element directamente, si es necesario)

## Criterios de Aceptación

*   Todos los Web Components de botones (`app-button-blue`, `app-button-red`, `app-button-green`) tienen un ancho visualmente uniforme.
*   Los botones del menú principal tienen un `min-width` de al menos `140px`.
*   Los botones dentro de los formularios y vistas de detalles se ajustan a un ancho adecuado dentro de su contenedor (similar al comportamiento anterior).
*   No hay errores en la consola del navegador.
*   La funcionalidad de los botones se mantiene.
