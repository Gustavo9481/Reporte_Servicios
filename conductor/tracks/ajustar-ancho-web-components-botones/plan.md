# Plan de Implementación: Ajustar ancho de Web Components de botones

## Tarea

Modificar los Web Components de botones (`app-button-blue`, `app-button-red`, `app-button-green`) para aplicar un ancho consistente, replicando el comportamiento de los botones HTML estándar anteriores, especialmente en el menú principal y en los formularios.

## Archivos a Modificar

*   `interface/components/app-button-blue/app-button-blue.js`
*   `interface/components/app-button-red/app-button-red.js`
*   `interface/components/app-button-green/app-button-green.js`
*   `interface/css/styles.css` (para aplicar estilos al host del Custom Element donde sea necesario, por ejemplo, en `.menu-options`)
*   `interface/index.html` (para actualizar la versión del script principal)

## Pasos

### 1. Modificar `interface/components/app-button-blue/app-button-blue.js`

*   Dentro de la etiqueta `<style>` del `shadowRoot`, añadir:
    ```css
    :host {
        display: inline-block; /* Permite aplicar ancho al custom element */
    }
    button {
        /* ... estilos existentes ... */
        min-width: 140px; /* Para los botones de menú */
        width: 100%; /* Permite que el botón ocupe el 100% del espacio del host si se establece un ancho externo */
        box-sizing: border-box; /* Asegura que padding y borde no aumenten el ancho total */
    }
    ```
    **Nota**: El `min-width` es para que los botones no sean demasiado pequeños por defecto, y `width: 100%` en el botón interno hará que se ajuste al ancho del `:host` o de su contenedor.

### 2. Modificar `interface/components/app-button-red/app-button-red.js`

*   Aplicar los mismos estilos CSS al `<style>` interno del `shadowRoot` que en `app-button-blue.js`.

### 3. Modificar `interface/components/app-button-green/app-button-green.js`

*   Aplicar los mismos estilos CSS al `<style>` interno del `shadowRoot` que en `app-button-blue.js`.

### 4. Modificar `interface/css/styles.css`

*   Añadir estilos para que los Custom Elements de botones se comporten como los botones originales en el `.menu-options` y en `.form-actions`.

    *   **Para el menú principal**:
        Reemplazar:
        ```css
        .menu-options button {
            padding: 8px 14px;
            font-size: 13px;
            min-width: 140px;
            width: auto;
        }
        ```
        Por (aplicando al Custom Element directamente, si es necesario, o asegurando que el host se comporte como `button`):
        ```css
        .menu-options app-button-blue { /* Aplicar al host del custom element */
            min-width: 140px;
            width: auto; /* Dejar que el custom element defina su ancho si es posible */
        }
        ```
        **Consideración**: Si `display: inline-block` en `:host` y `width: 100%` en el `button` interno ya resuelven esto, es posible que solo necesitemos ajustar el `display` del contenedor. Si el `min-width` en el botón interno es suficiente, no necesitaríamos este paso. La idea es que los Custom Elements (`app-button-blue`) dentro de `.menu-options` se comporten como lo hacían los `<button>` originales en términos de `flex` y `gap`. Esto ya lo estamos logrando con `display: inline-block` en `:host` y el `min-width` interno.

    *   **Para botones dentro de `reports-table td` (ej. "Ver Detalles")**:
        Reemplazar:
        ```css
        .reports-table td button {
            margin-right: 5px;
            padding: 4px 8px;
            font-size: 12px;
            min-width: auto;
        }
        ```
        Por:
        ```css
        .reports-table td app-button-blue,
        .reports-table td app-button-red,
        .reports-table td app-button-green {
            margin-right: 5px;
            padding: 4px 8px; /* Mantener el padding pequeño para la tabla */
            font-size: 12px;
            min-width: auto; /* Permitir que se ajuste al contenido, o un min-width menor */
        }
        ```

    *   **Para botones dentro de `.form-actions` (ej. "Cancelar", "Guardar", "Actualizar")**:
        Reemplazar:
        ```css
        .form-actions button {
            padding: 8px 14px;
            font-size: 13px;
            min-width: 140px;
        }
        ```
        Por:
        ```css
        .form-actions app-button-blue,
        .form-actions app-button-red,
        .form-actions app-button-green {
            padding: 8px 14px;
            font-size: 13px;
            min-width: 140px;
        }
        ```
    *   **Para botones `.btn-add` y `.btn-remove` (en formularios dinámicos)**:
        Estos ya tienen un `min-width: auto;` y `width: auto;`. Deberíamos aplicarles estilos similares a sus Custom Elements.
        ```css
        .btn-add,
        .btn-remove { /* Ya se aplican estos estilos */
            min-width: auto;
            width: auto;
        }
        ```
        Necesitamos asegurarnos de que los Custom Elements (`app-button-blue`, `app-button-red`) que ahora llevan estas clases reciban los estilos.

### 5. Modificar `interface/index.html`

*   Incrementar la versión del script principal (`scripts.js`) para forzar la recarga del navegador.

## Verificación

*   Recargar la aplicación en el navegador.
*   Navegar por las diferentes vistas y formularios.
*   Verificar visualmente que los botones (`app-button-blue`, `app-button-red`, `app-button-green`) tienen un ancho uniforme y consistente con el diseño anterior.
*   Asegurarse de que el `min-width: 140px` se aplica a los botones del menú principal y que los botones de formularios se ajustan correctamente.
*   Verificar que la funcionalidad de los botones se mantiene.
*   Abrir la consola del navegador y verificar que no hay errores de JavaScript.

Comenzaré con el Paso 1: Modificar `interface/components/app-button-blue/app-button-blue.js`. Para ello, primero leeré el archivo.
