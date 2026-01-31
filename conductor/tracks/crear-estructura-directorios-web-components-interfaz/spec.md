# Especificación: Crear estructura de directorios para Web Components en la interfaz

## Objetivo

Establecer una estructura de directorios organizada dentro de la carpeta `interface/` para albergar futuros Web Components, siguiendo un enfoque modular y escalable. Esto sentará las bases para la migración gradual de la interfaz a un paradigma de componentes.

## Requisitos

1.  **Crear directorios principales**: Dentro de `interface/`, se deben crear los siguientes directorios:
    *   `components/`: Para almacenar Web Components genéricos y reutilizables.
    *   `pages/`: Para componentes o scripts específicos de cada vista principal de la aplicación.
    *   `utils/`: Para funciones de utilidad o helpers compartidos.
    *   `styles/`: Para hojas de estilo globales o variables de CSS, sin mover el `styles.css` actual.
    *   `assets/`: Para imágenes, iconos, o cualquier otro recurso estático que los componentes puedan necesitar.
2.  **No modificar archivos existentes**: Los archivos `interface/css/styles.css`, `interface/js/scripts.js` e `interface/index.html` deben permanecer en sus ubicaciones actuales y sin modificaciones en su contenido, salvo lo estrictamente necesario para la inclusión de nuevos componentes o módulos en el futuro (lo cual no será parte de esta tarea).
3.  **No crear archivos placeholder**: Esta tarea se limita a la creación de la estructura de directorios; no se deben crear archivos placeholder dentro de estos nuevos directorios en esta fase.

## Archivos Afectados

*   `interface/` (se añadirán nuevos directorios dentro de este).

## Criterios de Aceptación

*   Los directorios `interface/components`, `interface/pages`, `interface/utils`, `interface/styles` y `interface/assets` existen.
*   Ningún archivo existente en `interface/` ha sido movido o modificado.
*   No se han creado archivos nuevos más allá de los directorios.
*   La estructura de directorios refleja una organización lógica para el desarrollo de Web Components.
