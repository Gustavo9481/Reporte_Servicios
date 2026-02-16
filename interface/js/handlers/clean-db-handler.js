// MÓDULO: interface/js/handlers/clean-db-handler.js
// Maneja la vista y lógica para limpiar la base de datos.

import { showContent } from "../utils/dom-utils.js";
import { fetchReportsPaginated } from "../main.js";

const contentArea = document.getElementById("contentArea");

/**
 * Renderiza la vista de confirmación para limpiar la base de datos.
 */
export const renderCleanDBView = () => {
    // Generación de código aleatorio simple (4 dígitos)
    const securityCode = Math.floor(1000 + Math.random() * 9000).toString();

    const html = `
        <h2>⚠️ Limpiar Base de Datos</h2>
        <div class="clean-db-container" style="max-width: 500px; margin: 0 auto; text-align: center; padding: 20px; border: 1px solid #ffcccc; background-color: #fff5f5; border-radius: 8px;">
            <p style="color: #cc0000; font-weight: bold;">ADVERTENCIA: Esta acción es irreversible.</p>
            <p>Se eliminarán los <span style="font-weight: bold;">10 registros más antiguos</span> de la base de datos.</p>
            
            <div style="margin: 20px 0;">
                <p>Para confirmar, ingrese el siguiente código:</p>
                <div style="font-size: 2em; font-weight: bold; letter-spacing: 5px; color: #333; background: #eee; padding: 10px; display: inline-block; border-radius: 5px;">
                    ${securityCode}
                </div>
            </div>

            <input type="text" id="inputSecurityCode" placeholder="Ingrese el código aquí" 
                   style="font-size: 1.2em; text-align: center; padding: 10px; width: 200px; margin-bottom: 20px;">
            <br>

            <div class="actions" style="display: flex; gap: 10px; justify-content: center;">
                 <app-button-blue id="btnCancelClean" type="button">Cancelar</app-button-blue>
                 <app-button-red id="btnConfirmClean" type="button">CONFIRMAR BORRADO</app-button-red>
            </div>
        </div>
    `;

    showContent(contentArea, html);

    console.log("DEBUG: Vista de limpieza renderizada. Código:", securityCode);

    // Event Listeners
    document.getElementById("btnCancelClean").addEventListener("click", () => {
        console.log("DEBUG: Click en Cancelar");
        showContent(contentArea, `<p style="text-align: center;">Operación cancelada.</p>`);
    });

    document.getElementById("btnConfirmClean").addEventListener("click", async () => {
        const inputCode = document.getElementById("inputSecurityCode").value;

        if (inputCode !== securityCode) {
            alert("❌ Código incorrecto. Verifique e intente nuevamente.");
            return;
        }

        // Ejecución directa de la limpieza (el código ya es la confirmación)
        try {
            const response = await fetch("/reportes/clean", {
                method: "DELETE"
            });

            const data = await response.json();

            if (response.ok) {
                alert(`✅ ${data.message}`);
                fetchReportsPaginated(1); // Redirigir a la lista de reportes
            } else {
                alert(`❌ Error al limpiar base de datos: ${data.detail || "Error desconocido"}`);
            }
        } catch (error) {
            console.error("Error de red:", error);
            alert("❌ Error de comunicación con el servidor.");
        }
    });
};
