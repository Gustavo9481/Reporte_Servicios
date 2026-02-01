# Plan de Implementación: Modularizar `scripts.js`

El objetivo de este plan es refactorizar el archivo `interface/js/scripts.js` en módulos más pequeños y manejables, siguiendo la propuesta del usuario. Cada sección de funcionalidad se extraerá a su propio archivo, y `scripts.js` actuará como el punto de entrada principal que orquesta los módulos.

Se procederá paso a paso, probando la funcionalidad después de cada refactorización importante.

## Fase 1: Preparación del Entorno

1.  **Crear el directorio de módulos**:
    *   Crear una nueva carpeta en `interface/js/modules/`.

2.  **Habilitar `scripts.js` como módulo**:
    *   En `interface/index.html`, modificar la etiqueta `<script>` que carga `scripts.js` para que incluya el atributo `type="module"`.
    *   Esto es esencial para poder usar `import` y `export`.

## Fase 2: Mover utilidades básicas

1.  **Crear `domUtils.js`**:
    *   Crear el archivo `interface/js/modules/domUtils.js`.
    *   Mover la función `showContent` de `scripts.js` a este nuevo archivo y exportarla.
    *   Importar `showContent` en `scripts.js`.

## Fase 3: Modularizar la Gestión de Reportes

1.  **Crear `reportManager.js`**:
    *   Crear el archivo `interface/js/modules/reportManager.js`.
    *   Mover las funciones `renderReportList`, `showReportDetails`, y `renderEditReportForm` desde `scripts.js` al nuevo módulo.
    *   **Manejo de Dependencias**: Estas funciones dependen de `contentArea`, de `showContent` y de otras funciones. Se refactorizarán para aceptar estas dependencias como argumentos.
    *   Exportar las funciones refactorizadas.

2.  **Integrar `reportManager.js`**:
    *   En `scripts.js`, importar las funciones de `reportManager.js`.
    *   Actualizar los *event listeners* para que llamen a las nuevas funciones importadas, pasándoles las dependencias necesarias.
    *   **PRUEBA**: Verificar que la lista de reportes, la vista de detalles y la edición de reportes sigan funcionando.

## Fase 4: Modularizar el Formulario de Nuevo Reporte

1.  **Crear `newReportManager.js`**:
    *   Crear el archivo `interface/js/modules/newReportManager.js`.
    *   Mover toda la lógica del *event listener* del botón `btnNuevoReporte` a una función de inicialización en este módulo (e.g., `initNewReportButton`).
    *   Manejar las dependencias (como `showReportDetails`) importándolas desde `reportManager.js`.

2.  **Integrar `newReportManager.js`**:
    *   En `scripts.js`, importar y llamar a la función `initNewReportButton`, pasándole las dependencias necesarias.
    *   **PRUEBA**: Verificar que el botón "Nuevo Reporte" abre el formulario y que este funciona correctamente.

## Fase 5: Modularizar los Formularios de Consulta

1.  **Crear `queryManager.js`**:
    *   Crear el archivo `interface/js/modules/queryManager.js`.
    *   Mover la lógica de los *event listeners* de `btnConsultarReporte`, `btnConsultarPlaca`, y `btnConsultarCliente` a una función de inicialización (e.g., `initQueryButtons`).
    *   Manejar dependencias, importando `renderReportList` y `showReportDetails` desde `reportManager.js`.

2.  **Integrar `queryManager.js`**:
    *   En `scripts.js`, importar y llamar a la función `initQueryButtons`.
    *   **PRUEBA**: Verificar que todas las funciones de consulta funcionan como se espera.

## Fase 6: Limpieza Final

1.  **Revisar `scripts.js`**:
    *   El archivo final `scripts.js` debe ser muy conciso. Su única responsabilidad debe ser obtener los elementos del DOM, importar los módulos y llamar a sus funciones de inicialización.

2.  **Actualizar versión**:
    *   Incrementar el número de versión en `index.html` para reflejar los cambios finales.
