# Guía de Inicio Rápido: Reporte de Servicios (Windows)

¡Bienvenido a la aplicación de **Reporte de Servicios**! Esta guía te ayudará a poner en marcha la aplicación en tu computadora con Windows de manera sencilla, sin necesidad de instalar Python ni configurar entornos complejos.

## 1. Requisitos Previos

No necesitas instalar herramientas adicionales como Python o bases de datos por separado. Todo lo necesario para que la aplicación funcione está incluido en el paquete que has recibido.

## 2. Instrucciones de Ejecución

Sigue estos pasos para iniciar la aplicación:

1.  **Localiza el archivo**: Busca el archivo llamado `Reporte_Servicios.exe` en la carpeta donde descargaste o descomprimiste el proyecto (generalmente dentro de una carpeta llamada `dist`).
2.  **Inicia la aplicación**: Haz doble clic sobre `Reporte_Servicios.exe`.
3.  **Ventana de Consola**: Se abrirá una ventana negra (consola). **No la cierres**. Esta ventana es el "motor" que mantiene la aplicación funcionando. Puedes minimizarla si quieres, pero si la cierras, la aplicación dejará de funcionar.
4.  **Acceso Automático**: Unos segundos después de abrir el archivo, tu navegador web predeterminado (Chrome, Edge, Firefox, etc.) se abrirá automáticamente en la dirección:  
    `http://127.0.0.1:8000`

## 3. Uso de la Aplicación

Una vez que veas la interfaz en tu navegador, ya puedes comenzar a gestionar tus reportes:
- La aplicación guardará todos tus datos automáticamente en un archivo de base de datos local llamado `reportes.db` que se creará en la misma carpeta del ejecutable.
- Puedes generar tus reportes en PDF y ver el estado de la conexión en el panel principal.

## 4. Cómo Cerrar la Aplicación

Para terminar de usar la aplicación de forma segura:

1.  Cierra la pestaña o ventana del navegador donde estabas trabajando.
2.  Ve a la ventana negra (consola) que se abrió al principio.
3.  Presiona las teclas `Ctrl + C` en tu teclado o simplemente cierra la ventana haciendo clic en la `X` de la esquina superior derecha.

---
**Nota Técnica:** Si el navegador no se abre automáticamente, puedes escribir manualmente `http://127.0.0.1:8000` en la barra de direcciones de cualquier navegador mientras la consola esté abierta.

*Desarrollado con ❤️ por GUScode*
