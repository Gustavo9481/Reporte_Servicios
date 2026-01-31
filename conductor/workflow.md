# Workflow: Reporte de Servicios

## Flujo de Desarrollo General

1.  **Entendimiento de Requisitos**: Clarificación de la funcionalidad deseada o el problema a resolver.
2.  **Planificación (Conductor Track)**:
    *   Creación de un nuevo "track" en Conductor para la tarea.
    *   Definición de una especificación detallada (`spec.md`).
    *   Desarrollo de un plan de implementación paso a paso (`plan.md`).
3.  **Implementación**:
    *   Desarrollo de la lógica del backend (modelos, endpoints de FastAPI).
    *   Implementación de la lógica del frontend (HTML, CSS, JavaScript) para interactuar con la API.
    *   Escritura de tests unitarios/integración según sea necesario.
    *   Asegurar que el código se adhiera a las convenciones definidas en `tech-stack.md`.
4.  **Pruebas Locales**:
    *   Ejecución de la aplicación localmente (`uvicorn main:app --reload`) para pruebas manuales.
    *   Ejecución de tests (`pytest`).
5.  **Revisión y Refactorización**: Revisar el código para optimización, claridad y adherencia a las buenas prácticas.
6.  **Validación**: Asegurar que la funcionalidad cumple con la especificación original.

## Proceso de Testing

*   **Tests de Unidad/Integración**: Se utilizará `pytest` para escribir y ejecutar pruebas automatizadas. Se recomienda escribir pruebas para la lógica crítica de la API y la interacción con la base de datos.
*   **Pruebas Manuales**: Para la interfaz de usuario, se realizarán pruebas manuales para verificar la interactividad y la corrección visual.

## Despliegue (Actual)

*   La aplicación se ejecuta localmente usando `uvicorn main:app --reload`.
*   La base de datos SQLite (`dB.sqlite3`) se gestiona localmente.

## Control de Versiones

*   **Git**: Se utilizará Git para el control de versiones.
*   **Commits**: Los mensajes de commit deben ser claros y concisos, describiendo el propósito del cambio.

## Reporte de Errores / Feedback

*   Los errores y el feedback se gestionarán según lo defina el usuario.
