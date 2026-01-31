# Especificación: Definir variables CSS globales para la paleta de colores

## Objetivo

Centralizar la gestión de la paleta de colores de la interfaz mediante variables CSS globales, facilitando la consistencia visual y el mantenimiento futuro. Esto es un paso preparatorio para la creación de Web Components.

## Requisitos

1.  **Ubicación**: Las variables CSS deben ser definidas en el archivo `interface/css/styles.css`.
2.  **Alcance**: Deben ser variables globales, declaradas dentro del selector `:root`.
3.  **Variables a definir**:
    *   `--blue-color`: Color azul principal.
    *   `--red-color`: Color rojo principal.
    *   `--green-color`: Color verde principal.
    *   `--grey-color`: Color gris principal (para texto o fondos).
    *   `--white-color`: Color blanco.
    *   `--black-color`: Color negro.
4.  **Valores**: Los valores de color deben basarse en la paleta de colores actualmente utilizada en el archivo `styles.css` para mantener la coherencia visual existente.
    *   `--blue-color`: `#4361ee` (basado en el color de los botones generales)
    *   `--red-color`: `#c1121f` (basado en el color de los botones `btn-remove` y `btn-generar-pdf`)
    *   `--green-color`: `#2a9d8f` (basado en el color de `btn-ver-detalles` y `form-actions button[type="submit"]`)
    *   `--grey-color`: `#333` (basado en el color del texto principal)
    *   `--white-color`: `white`
    *   `--black-color`: `black`

## Archivos Afectados

*   `interface/css/styles.css`

## Criterios de Aceptación

*   El archivo `interface/css/styles.css` contiene las variables CSS especificadas dentro del selector `:root`.
*   Los valores asignados a las variables corresponden a la paleta de colores existente en la aplicación.
*   No se introduce ningún cambio visual en la interfaz existente como resultado de la adición de estas variables (ya que solo se definen, no se usan aún).
*   El resto del archivo `styles.css` permanece intacto, salvo la adición de estas líneas.
