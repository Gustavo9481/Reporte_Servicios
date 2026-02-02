// MÓDULO: interface/js/handlers/report-list-handler.js
import { showContent } from "../utils/dom-utils.js";
import { showReportDetails } from "./report-details-handler.js";

const contentArea = document.getElementById("contentArea");

// --- FUNCIÓN PARA RENDERIZAR LA LISTA DE REPORTES EN UNA TABLA CON PAGINACIÓN ---
export const renderReportList = (reports, currentPage, itemsPerPage, totalReports, onPageChange) => {
  let html = "<h2>Listado de Reportes</h2>";
  if (reports.length === 0 && totalReports === 0) {
    html += "<p>No hay reportes registrados.</p>";
    showContent(contentArea, html);
    return;
  } else if (reports.length === 0 && totalReports > 0) {
    html += "<p>No hay reportes en esta página.</p>";
  }

  html += '<table class="reports-table">';
  html +=
    '<thead><tr><th>ID</th><th>Placa</th><th>Cliente</th><th>Fecha</th><th class="text-right">Total</th><th class="text-center">Estado</th><th>Acciones</th></tr></thead>';
  html += "<tbody>";
  reports.forEach((report) => {
    html += `
              <tr>
                  <td>${report.id_reporte}</td>
                  <td>${report.placa}</td>
                  <td>${report.nombre_cliente}</td>
                  <td>${report.fecha}</td>
                  <td class="text-right">${(report.total_general || 0).toFixed(2)}</td>
                   <td class="text-center"><app-status-badge status="${report.status_reporte}"></app-status-badge></td>
                  <td>
                      <app-button-view-details data-id="${report.id_reporte}">Ver Detalles</app-button-view-details>
                  </td>
              </tr>
          `;
  });
  html += "</tbody></table>";

  // Lógica de Paginación
  const totalPages = Math.ceil(totalReports / itemsPerPage);
  if (totalPages > 1) {
    html += `<div class="pagination-controls">`;
    html += `<app-button-pagination-next id="prevPage" ${currentPage === 1 ? "disabled" : ""}>&lt;</app-button-pagination-next>`;
    html += `<span class="pagination-info">Página ${currentPage} de ${totalPages} (Total: ${totalReports} reportes)</span>`;
    html += `<app-button-pagination-next id="nextPage" ${currentPage === totalPages ? "disabled" : ""}>&gt;</app-button-pagination-next>`;
    html += `</div>`;
  }

  showContent(contentArea, html);

  // Añadir event listeners a los nuevos botones "Ver Detalles"
  document.querySelectorAll("app-button-view-details").forEach((button) => {
    button.addEventListener("click", (event) => {
      const reporteId = event.target.dataset.id;
      showReportDetails(reporteId);
    });
  });

  // Event listeners para los controles de paginación
  if (totalPages > 1) {
    document.getElementById("prevPage").addEventListener("click", () => {
      if (currentPage > 1) {
        onPageChange(currentPage - 1);
      }
    });

    document.getElementById("nextPage").addEventListener("click", () => {
      if (currentPage < totalPages) {
        onPageChange(currentPage + 1);
      }
    });
  }
};
