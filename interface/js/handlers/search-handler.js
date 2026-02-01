// MÓDULO: interface/js/handlers/search-handler.js
import { showContent } from "../utils/dom-utils.js";
import { showReportDetails } from "./report-details-handler.js";
import { renderReportList } from "./report-list-handler.js";

const contentArea = document.getElementById("contentArea");

export const renderSearchByIdForm = () => {
  let html = `
          <h2>Consultar Reporte por ID</h2>
          <div class="form-container">
              <input type="text" id="reporteIdInput" placeholder="Introduce el ID del reporte" />
              <app-button-blue id="btnBuscarReporte">Buscar</app-button-blue>
          </div>
      `;
  showContent(contentArea, html);
  document.getElementById("btnBuscarReporte").addEventListener("click", async () => {
    const reporteId = document.getElementById("reporteIdInput").value;
    if (!reporteId) {
      showContent(contentArea, '<p class="error-message">Por favor, introduce un ID de reporte.</p>');
      return;
    }
    showReportDetails(reporteId);
  });
};

export const renderSearchByPlacaForm = () => {
  let html = `
          <h2>Consultar Reportes por Placa de Vehículo</h2>
          <div class="form-container">
              <input type="text" id="placaInput" placeholder="Introduce la placa (ej: ABC12D)" />
              <app-button-blue id="btnBuscarPlaca">Buscar</app-button-blue>
          </div>
      `;
  showContent(contentArea, html);
  document.getElementById("btnBuscarPlaca").addEventListener("click", async () => {
    const placa = document.getElementById("placaInput").value;
    if (!placa) {
      showContent(contentArea, '<p class="error-message">Por favor, introduce una placa.</p>');
      return;
    }
    showContent(contentArea, `<p>Cargando reportes para la placa: ${placa}...</p>`);
    try {
      const response = await fetch(`/reportes/placa/${placa}`);
      const data = await response.json();
      if (response.ok) {
        renderReportList(data);
      } else {
        showContent(
          contentArea,
          `<p class="error-message">Error: ${data.detail || "No se encontraron reportes para esta placa."}</p>`,
        );
      }
    } catch (error) {
      showContent(contentArea, `<p class="error-message">Error de red: ${error.message}`);
    }
  });
};

export const renderSearchByClientForm = () => {
  let html = `
          <h2>Consultar Reportes por Cliente</h2>
          <div class="form-container" style="display: flex; flex-direction: column; gap: 10px; max-width: 400px; margin: 0 auto;">
              <input type="number" id="cedulaClienteInput" placeholder="Buscar por Cédula" />
              <input type="text" id="nombreClienteInput" placeholder="Buscar por Nombre" />
              <input type="number" id="telefonoClienteInput" placeholder="Buscar por Teléfono" />
              <app-button-blue id="btnBuscarCliente" style="margin-top: 10px;">Buscar</app-button-blue>
          </div>
      `;
  showContent(contentArea, html);
  document.getElementById("btnBuscarCliente").addEventListener("click", async () => {
    const cedula = document.getElementById("cedulaClienteInput").value;
    const nombre = document.getElementById("nombreClienteInput").value;
    const telefono = document.getElementById("telefonoClienteInput").value;

    let url = "";
    let searchMsg = "";

    if (cedula) {
      url = `/reportes/cliente/${cedula}`;
      searchMsg = `cédula: ${cedula}`;
    } else if (nombre) {
      url = `/reportes/cliente/nombre/${encodeURIComponent(nombre)}`;
      searchMsg = `nombre: ${nombre}`;
    } else if (telefono) {
      url = `/reportes/cliente/telefono/${telefono}`;
      searchMsg = `teléfono: ${telefono}`;
    } else {
      alert("Por favor, introduce al menos un criterio de búsqueda (Cédula, Nombre o Teléfono).");
      return;
    }

    showContent(contentArea, `<p>Cargando reportes para ${searchMsg}...</p>`);
    try {
      const response = await fetch(url);
      const data = await response.json();
      if (response.ok) {
        renderReportList(data);
      } else {
        alert("Por favor, introduce al menos un criterio de búsqueda (Cédula, Nombre o Teléfono).");
        showContent(
          contentArea,
          `<p class="error-message">Error: ${data.detail || "No se encontraron reportes para esta búsqueda."}</p>`,
        );
      }
    } catch (error) {
      showContent(contentArea, `<p class="error-message">Error de red: ${error.message}`);
    }
  });
};
