// MODULO: interface/js/main.js

import { renderNewReportForm } from "./handlers/new-report-form-handler.js";
import { renderReportList } from "./handlers/report-list-handler.js";
import { renderSearchByIdForm, renderSearchByPlacaForm, renderSearchByClientForm } from "./handlers/search-handler.js";
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
const fetchReportsPaginated = async (page) => {
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
  // Inicializar referencias a los elementos del DOM una vez que el DOM esté cargado
  btnNuevoReporte = document.getElementById("btnNuevoReporte");
  btnConsultarReporte = document.getElementById("btnConsultarReporte");
  btnConsultarPlaca = document.getElementById("btnConsultarPlaca");
  btnConsultarCliente = document.getElementById("btnConsultarCliente");
  btnListaReportes = document.getElementById("btnListaReportes");
  contentArea = document.getElementById("contentArea");

  // --- Event Listeners para los botones del menú ---
  if (btnNuevoReporte) {
    btnNuevoReporte.addEventListener("click", () => {
      renderNewReportForm();
    });
  }

  if (btnConsultarReporte) {
    btnConsultarReporte.addEventListener("click", () => {
      renderSearchByIdForm();
    });
  }

  if (btnConsultarPlaca) {
    btnConsultarPlaca.addEventListener("click", () => {
      renderSearchByPlacaForm();
    });
  }

  if (btnConsultarCliente) {
    btnConsultarCliente.addEventListener("click", () => {
      renderSearchByClientForm();
    });
  }

  if (btnListaReportes) {
    btnListaReportes.addEventListener("click", () => {
      fetchReportsPaginated(1); // Cargar la primera página al hacer clic en "Lista de Reportes"
    });
  }
});
