// MODULO: interface/js/handlers/report-details-handler.js

// Manejador para interfaz de 'Detalles de Reporte'.


import { showContent } from "../utils/dom-utils.js";
import { renderEditReportForm } from "./edit-report-form-handler.js"; // Se importará una vez exista
import { renderReportList } from "./report-list-handler.js";

const contentArea = document.getElementById("contentArea");

export const showReportDetails = async (reporteId) => {
  showContent(contentArea, `<p>Cargando detalles del reporte ID: ${reporteId}...</p>`);
  try {
    const response = await fetch(`/reportes/${reporteId}`);
    const data = await response.json();

    if (response.ok) {
      let html = `
                  <div class="report-detail-view">
                      <h2>Detalles del Reporte #${data.id_reporte}</h2>

                      <h3>Información General</h3>
                      <table class="details-table">
                          <tr><th>Placa</th><td>${data.placa}</td></tr>
                          <tr><th>Modelo</th><td>${data.modelo}</td></tr>
                          <tr><th>Color</th><td>${data.color}</td></tr>
                          <tr><th>Fecha</th><td>${data.fecha}</td></tr>
                          <tr><th class="text-center">Estado</th> <td class="text-center"><app-status-badge status="${data.status_reporte}"></app-status-badge></td></tr>
                          <tr><th>Factura Reporte</th><td>${data.factura_reporte || "N/A"}</td></tr>
                          <tr><th>Monto Factura</th><td>${data.factura_monto !== null ? data.factura_monto : "N/A"}</td></tr>
                      </table>

                      <h3>Datos del Cliente</h3>
                      <table class="details-table">
                          <tr><th>Nombre</th><td>${data.nombre_cliente}</td></tr>
                          <tr><th>Cédula</th><td>${data.cedula_cliente}</td></tr>
                          <tr><th>Teléfono</th><td>${data.telefono_cliente}</td></tr>
                      </table>

                      <h3>Carrocería</h3>
                      <table class="details-table checklist-table">
                          <tr>
                              <td class="${data.carroceria_golpe ? "check-true" : "check-false"}">Golpe: ${data.carroceria_golpe ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.carroceria_suelto ? "check-true" : "check-false"}">Suelto: ${data.carroceria_suelto ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                          <tr>
                              <td class="${data.carroceria_rayas ? "check-true" : "check-false"}">Rayas: ${data.carroceria_rayas ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.carroceria_desconchado ? "check-true" : "check-false"}">Desconchado: ${data.carroceria_desconchado ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                          <tr>
                              <td class="${data.carroceria_vidrio_roto ? "check-true" : "check-false"}">Vidrio Roto: ${data.carroceria_vidrio_roto ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.carroceria_falta_moldura ? "check-true" : "check-false"}">Falta Moldura: ${data.carroceria_falta_moldura ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                          <tr>
                              <td class="${data.carroceria_falta_faro ? "check-true" : "check-false"}">Falta Faro: ${data.carroceria_falta_faro ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.carroceria_falta_accesorio ? "check-true" : "check-false"}">Falta Accesorio: ${data.carroceria_falta_accesorio ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                          <tr>
                              <td class="${data.carroceria_espejo_roto ? "check-true" : "check-false"}">Espejo Roto: ${data.carroceria_espejo_roto ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.carroceria_falta_centro_copas ? "check-true" : "check-false"}">Falta Centro Copas: ${data.carroceria_falta_centro_copas ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                          <tr>
                              <td colspan="2" class="${data.carroceria_otro ? "check-true" : "check-false"}">Otro (Carrocería): ${data.carroceria_otro ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                      </table>

                      <h3>Accesorios</h3>
                      <table class="details-table checklist-table">
                          <tr>
                              <td class="${data.accesorios_alfombra_delantera ? "check-true" : "check-false"}">Alfombra Del: ${data.accesorios_alfombra_delantera ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.accesorios_alfombra_trasera ? "check-true" : "check-false"}">Alfombra Tras: ${data.accesorios_alfombra_trasera ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                          <tr>
                              <td class="${data.accesorios_radio ? "check-true" : "check-false"}">Radio: ${data.accesorios_radio ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.accesorios_radio_reproductor ? "check-true" : "check-false"}">Reproductor: ${data.accesorios_radio_reproductor ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                          <tr>
                              <td class="${data.accesorios_antena_electrica ? "check-true" : "check-false"}">Antena Eléc: ${data.accesorios_antena_electrica ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.accesorios_encendedor_cigarrillos ? "check-true" : "check-false"}">Encendedor: ${data.accesorios_encendedor_cigarrillos ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                          <tr>
                              <td class="${data.accesorios_triangulo_seguridad ? "check-true" : "check-false"}">Triángulo Seg: ${data.accesorios_triangulo_seguridad ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.accesorios_gato ? "check-true" : "check-false"}">Gato: ${data.accesorios_gato ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                          <tr>
                              <td class="${data.accesorios_caucho_repuesto ? "check-true" : "check-false"}">Caucho Rep: ${data.accesorios_caucho_repuesto ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.accesorios_otro ? "check-true" : "check-false"}">Otro (Accesorios): ${data.accesorios_otro ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                      </table>

                      <h3>Sistemas Eléctricos</h3>
                      <table class="details-table checklist-table">
                          <tr>
                              <td class="${data.sistem_electric_frenos_del ? "check-true" : "check-false"}">Frenos Del: ${data.sistem_electric_frenos_del ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.sistem_electric_tablero ? "check-true" : "check-false"}">Tablero: ${data.sistem_electric_tablero ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                          <tr>
                              <td class="${data.sistem_electric_luz_cruce ? "check-true" : "check-false"}">Luz Cruce: ${data.sistem_electric_luz_cruce ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.sistem_electric_stop ? "check-true" : "check-false"}">Luz Stop: ${data.sistem_electric_stop ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                          <tr>
                              <td class="${data.sistem_electric_vidrio_electrico ? "check-true" : "check-false"}">Vidrio Eléc: ${data.sistem_electric_vidrio_electrico ? "<strong>SI</strong>" : "NO"}</td>
                              <td class="${data.sistem_electric_aire_acondicionado ? "check-true" : "check-false"}">Aire Acond: ${data.sistem_electric_aire_acondicionado ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                          <tr>
                              <td colspan="2" class="${data.sistem_electric_otro ? "check-true" : "check-false"}">Otro (Sist. Eléc): ${data.sistem_electric_otro ? "<strong>SI</strong>" : "NO"}</td>
                          </tr>
                      </table>
              `;

      if (data.observaciones) {
        html += `
                          <h3>Observaciones Adicionales</h3>
                          <p class="details-text">${data.observaciones}</p>
                      `;
      }

      if (data.servicios && data.servicios.length > 0) {
        html +=
          '<h3>Servicios Realizados</h3><table class="details-table"><thead><tr><th>Item</th><th>Descripción</th><th class="text-right">Presupuesto</th></tr></thead><tbody>';
        data.servicios.forEach((s) => {
          html += `<tr><td>${s.item}</td><td>${s.descripcion}</td><td class="text-right">${s.presupuesto.toFixed(2)}</td></tr>`;
        });
        html += "</tbody></table>";
      }

      if (data.repuestos && data.repuestos.length > 0) {
        html +=
          '<h3>Repuestos Utilizados</h3><table class="details-table"><thead><tr><th>Cantidad</th><th>Descripción</th><th class="text-right">Presupuesto</th></tr></thead><tbody>';
        data.repuestos.forEach((r) => {
          html += `<tr><td>${r.cantidad}</td><td>${r.descripcion}</td><td class="text-right">${r.presupuesto.toFixed(2)}</td></tr>`;
        });
        html += "</tbody></table>";
      }

      html += `
                      <h3>Resumen de Presupuesto</h3>
                      <table class="details-table summary-table">
                          <thead><tr><th>Concepto</th><th class="text-right">Monto</th></tr></thead>
                          <tbody>
                              <tr><td>Total Servicios</td><td class="text-right">${(data.total_servicios || 0).toFixed(2)}</td></tr>
                              <tr><td>Total Repuestos</td><td class="text-right">${(data.total_repuestos || 0).toFixed(2)}</td></tr>
                              <tr><td><strong>Total General</strong></td><td class="text-right"><strong>${(data.total_general || 0).toFixed(2)}</strong></td></tr>
                          </tbody>
                      </table>
                  `;

      html += `<div class="form-actions" style="margin-top: 20px; display: flex; gap: 10px; justify-content: flex-end;">`;
      html += `<app-button-blue id="btnVolverLista">Volver a la lista</app-button-blue>`;
      html += `<app-button-green id="btnEditarReporte">Editar Reporte</app-button-green>`;
      html += `<app-button-red id="btnGenerarPDF">Generar PDF</app-button-red>`;
      html += `</div></div>`;
      showContent(contentArea, html);

      document.getElementById("btnVolverLista").addEventListener("click", () => {
          const btnListaReportesMain = document.getElementById("btnListaReportes");
          if (btnListaReportesMain) {
              btnListaReportesMain.click(); // Esto activará la lógica de paginación en main.js
          } else {
              console.error("El botón 'Lista de Reportes' no se encontró en el DOM.");
          }
      });
      document.getElementById("btnEditarReporte").addEventListener("click", () => {
          renderEditReportForm(data);
      });
      document.getElementById("btnGenerarPDF").addEventListener("click", () => {
          const pdfUrl = `/reportes/${reporteId}/pdf`;
          window.open(pdfUrl, '_blank');
      });
    } else {
      showContent(contentArea, `<p>Error: ${data.detail}</p>`);
    }
  } catch (error) {
    showContent(contentArea, `<p>Error de red: ${error.message}</p>`);
  }
};
