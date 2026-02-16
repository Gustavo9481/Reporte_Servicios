// MODULO: interface/js/main.js

import { renderNewReportForm } from "./handlers/new-report-form-handler.js";
import { renderReportList } from "./handlers/report-list-handler.js";
import { renderSearchByIdForm, renderSearchByPlacaForm, renderSearchByClientForm } from "./handlers/search-handler.js";
import { renderCleanDBView } from "./handlers/clean-db-handler.js";
import { showContent } from "./utils/dom-utils.js";

// Referencias a los elementos del DOM (inicializadas dentro de DOMContentLoaded)
let btnNuevoReporte;
let btnConsultarReporte;
let btnConsultarPlaca;
let btnConsultarCliente;
let btnListaReportes;
let contentArea;

// Variables de estado para la paginación
let currentPage = 1;
const itemsPerPage = 15; // Mostrar 15 reportes por página

// Función para obtener y renderizar los reportes con paginación
export const fetchReportsPaginated = async (page) => {
  currentPage = page;
  const skip = (currentPage - 1) * itemsPerPage;
  const limit = itemsPerPage;

  showContent(contentArea, "<p>Cargando lista de reportes...</p>");
  try {
    const response = await fetch(`/reportes/?skip=${skip}&limit=${limit}`);
    const result = await response.json(); // Ahora esperamos un objeto { total_count, reports }

    if (response.ok) {
      renderReportList(
        result.reports,
        currentPage,
        itemsPerPage,
        result.total_count,
        fetchReportsPaginated // Pasar la función de cambio de página
      );
    } else {
      showContent(contentArea, `<p>Error al cargar reportes: ${result.detail}</p>`);
    }
  } catch (error) {
    showContent(contentArea, `<p>Error de red: ${error.message}</p>`);
  }
};

document.addEventListener("DOMContentLoaded", () => {
  // --- Event Listeners para los botones del menú ---

  // Nuevo Reporte
  const btnNuevoReporte = document.getElementById("btnNuevoReporte");
  if (btnNuevoReporte) {
    btnNuevoReporte.addEventListener("click", () => {
      renderNewReportForm();
    });
  }

  // Consultar por ID
  const btnConsultarReporte = document.getElementById("btnConsultarReporte");
  if (btnConsultarReporte) {
    btnConsultarReporte.addEventListener("click", () => {
      renderSearchByIdForm();
    });
  }

  // Consultar por Placa
  const btnConsultarPlaca = document.getElementById("btnConsultarPlaca");
  if (btnConsultarPlaca) {
    btnConsultarPlaca.addEventListener("click", () => {
      renderSearchByPlacaForm();
    });
  }

  // Consultar por Cliente
  const btnConsultarCliente = document.getElementById("btnConsultarCliente");
  if (btnConsultarCliente) {
    btnConsultarCliente.addEventListener("click", () => {
      renderSearchByClientForm();
    });
  }

  // Listar Reportes
  const btnListaReportes = document.getElementById("btnListaReportes");
  if (btnListaReportes) {
    btnListaReportes.addEventListener("click", () => {
      fetchReportsPaginated(1);
    });
  }

  // Limpiar Base de Datos (Nuevo Botón)
  const btnCleanDB = document.getElementById("btnCleanDB");
  if (btnCleanDB) {
    btnCleanDB.addEventListener("click", () => {
      renderCleanDBView();
    });
  }
});
