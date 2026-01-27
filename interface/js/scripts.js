// interface/js/scripts.js
document.addEventListener("DOMContentLoaded", () => {
  // Referencias a los elementos del DOM
  const btnNuevoReporte = document.getElementById("btnNuevoReporte");
  const btnConsultarReporte = document.getElementById("btnConsultarReporte");
  const btnConsultarCliente = document.getElementById("btnConsultarCliente");
  const btnListaReportes = document.getElementById("btnListaReportes");
  const contentArea = document.getElementById("contentArea");

  // Función para mostrar contenido HTML en el área principal
  const showContent = (htmlContent) => {
    contentArea.innerHTML = htmlContent;
  };

  // --- FUNCIÓN PARA RENDERIZAR LA LISTA DE REPORTES EN UNA TABLA ---
  const renderReportList = (reports) => {
    let html = "<h2>Listado de Reportes</h2>";
    if (reports.length === 0) {
      html += "<p>No hay reportes registrados.</p>";
      showContent(html);
      return;
    }

    html += '<table class="reports-table">';
    html +=
      "<thead><tr><th>ID</th><th>Placa</th><th>Cliente</th><th>Fecha</th><th>Total</th><th>Estado</th><th>Acciones</th></tr></thead>";
    html += "<tbody>";
    reports.forEach((report) => {
      html += `
                <tr>
                    <td>${report.id_reporte}</td>
                    <td>${report.placa}</td>
                    <td>${report.nombre_cliente}</td>
                    <td>${report.fecha}</td>
                    <td>${(report.total_general || 0).toFixed(2)}</td>
                    <td><span class="status ${report.status_reporte}">${report.status_reporte}</span></td>
                    <td>
                        <button class="btn-ver-detalles" data-id="${report.id_reporte}">Ver Detalles</button>
                    </td>
                </tr>
            `;
    });
    html += "</tbody></table>";
    showContent(html);

    // Añadir event listeners a los nuevos botones "Ver Detalles"
    document.querySelectorAll(".btn-ver-detalles").forEach((button) => {
      button.addEventListener("click", (event) => {
        const reporteId = event.target.dataset.id;
        showReportDetails(reporteId);
      });
    });
  };

  // --- FUNCIÓN PARA MOSTRAR DETALLES DE UN REPORTE ESPECÍFICO ---
  const showReportDetails = async (reporteId) => {
    showContent(`<p>Cargando detalles del reporte ID: ${reporteId}...</p>`);
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
                            <tr><th>Estado</th><td><span class="status ${data.status_reporte}">${data.status_reporte}</span></td></tr>
                            <tr><th>Factura Reporte</th><td>${data.factura_reporte || "N/A"}</td></tr>
                            <tr><th>Monto Factura</th><td>${data.factura_monto !== null ? data.factura_monto : "N/A"}</td></tr>
                        </table>

                        <h3>Datos del Cliente</h3>
                        <table class="details-table">
                            <tr><th>Nombre</th><td>${data.nombre_cliente}</td></tr>
                            <tr><th>Cédula</th><td>${data.cedula_cliente}</td></tr>
                            <tr><th>Teléfono</th><td>${data.telefono_cliente}</td></tr>
                        </table>

                        <h3>Checklist: Carrocería</h3>
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

                        <h3>Checklist: Accesorios</h3>
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

                        <h3>Checklist: Sistemas Eléctricos</h3>
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
            '<h3>Servicios Realizados</h3><table class="details-table"><thead><tr><th>Item</th><th>Descripción</th><th>Presupuesto</th></tr></thead><tbody>';
          data.servicios.forEach((s) => {
            html += `<tr><td>${s.item}</td><td>${s.descripcion}</td><td>${s.presupuesto.toFixed(2)}</td></tr>`;
          });
          html += "</tbody></table>";
        }

        if (data.repuestos && data.repuestos.length > 0) {
          html +=
            '<h3>Repuestos Utilizados</h3><table class="details-table"><thead><tr><th>Cantidad</th><th>Descripción</th><th>Presupuesto</th></tr></thead><tbody>';
          data.repuestos.forEach((r) => {
            html += `<tr><td>${r.cantidad}</td><td>${r.descripcion}</td><td>${r.presupuesto.toFixed(2)}</td></tr>`;
          });
          html += "</tbody></table>";
        }

        html += `
                    <h3>Resumen de Presupuesto</h3>
                    <table class="details-table summary-table">
                        <tr><th>Total Servicios</th><td>${(data.total_servicios || 0).toFixed(2)}</td></tr>
                        <tr><th>Total Repuestos</th><td>${(data.total_repuestos || 0).toFixed(2)}</td></tr>
                        <tr><th>Total General</th><td>${(data.total_general || 0).toFixed(2)}</td></tr>
                    </table>
                `;

        html += `<div class="form-actions" style="text-align: right; margin-top: 20px;">`;
        html += `<button id="btnVolverLista" style="background-color: #6c757d;">Volver a la lista</button>`;
        html += `<button id="btnEditarReporte" class="btn-editar">Editar Reporte</button>`;
        html += `<a href="/reportes/${reporteId}/pdf" target="_blank" class="btn-generar-pdf">Generar PDF</a>`;
        html += `</div></div>`;
        showContent(html);

        document.getElementById("btnVolverLista").addEventListener("click", () => btnListaReportes.click());
        document.getElementById("btnEditarReporte").addEventListener("click", () => renderEditReportForm(data));
      } else {
        showContent(`<p>Error: ${data.detail}</p>`);
      }
    } catch (error) {
      showContent(`<p>Error de red: ${error.message}</p>`);
    }
  };

  // --- FUNCIÓN PARA RENDERIZAR EL FORMULARIO DE EDICIÓN ---
  const renderEditReportForm = (report) => {
    let html = `
            <h2>Editar Reporte #${report.id_reporte}</h2>
            <form id="formEditReporte" class="report-form">
                 <div class="form-section">
                    <h3>Datos del Cliente y Vehículo</h3>
                    <div class="form-grid">
                        <input type="text" name="placa" placeholder="Placa" value="${report.placa}" required>
                        <input type="text" name="modelo" placeholder="Modelo" value="${report.modelo}" required>
                        <input type="text" name="color" placeholder="Color" value="${report.color}" required>
                        <input type="text" name="nombre_cliente" placeholder="Nombre del Cliente" value="${report.nombre_cliente}" required>
                        <input type="number" name="cedula_cliente" placeholder="Cédula" value="${report.cedula_cliente}" required>
                        <input type="number" name="telefono_cliente" placeholder="Teléfono" value="${report.telefono_cliente}" required>
                    </div>
                </div>

                <div class="form-section">
                    <h3>Estado y Facturación</h3>
                    <div class="form-grid">
                        <select name="status_reporte" required>
                            <option value="activa" ${report.status_reporte === "activa" ? "selected" : ""}>Activa</option>
                            <option value="anulada" ${report.status_reporte === "anulada" ? "selected" : ""}>Anulada</option>
                        </select>
                        <input type="text" name="factura_reporte" placeholder="Nº Factura (Opcional)" value="${report.factura_reporte || ""}">
                        <input type="number" step="0.01" name="factura_monto" placeholder="Monto Factura (Opcional)" value="${report.factura_monto || ""}">
                    </div>
                </div>

                <div class="form-section">
                    <h3>Checklist: Carrocería</h3>
                    <div class="checklist-form-grid">
                        <label><input type="checkbox" name="carroceria_golpe" ${report.carroceria_golpe ? "checked" : ""}> Golpe</label>
                        <label><input type="checkbox" name="carroceria_suelto" ${report.carroceria_suelto ? "checked" : ""}> Suelto</label>
                        <label><input type="checkbox" name="carroceria_rayas" ${report.carroceria_rayas ? "checked" : ""}> Rayas</label>
                        <label><input type="checkbox" name="carroceria_desconchado" ${report.carroceria_desconchado ? "checked" : ""}> Desconchado</label>
                        <label><input type="checkbox" name="carroceria_vidrio_roto" ${report.carroceria_vidrio_roto ? "checked" : ""}> Vidrio Roto</label>
                        <label><input type="checkbox" name="carroceria_falta_moldura" ${report.carroceria_falta_moldura ? "checked" : ""}> Falta Moldura</label>
                        <label><input type="checkbox" name="carroceria_falta_faro" ${report.carroceria_falta_faro ? "checked" : ""}> Falta Faro</label>
                        <label><input type="checkbox" name="carroceria_falta_accesorio" ${report.carroceria_falta_accesorio ? "checked" : ""}> Falta Accesorio</label>
                        <label><input type="checkbox" name="carroceria_espejo_roto" ${report.carroceria_espejo_roto ? "checked" : ""}> Espejo Roto</label>
                        <label><input type="checkbox" name="carroceria_falta_centro_copas" ${report.carroceria_falta_centro_copas ? "checked" : ""}> Falta Centro Copas</label>
                        <label><input type="checkbox" name="carroceria_otro" ${report.carroceria_otro ? "checked" : ""}> Otro</label>
                    </div>
                </div>

                <div class="form-section">
                    <h3>Checklist: Accesorios</h3>
                    <div class="checklist-form-grid">
                        <label><input type="checkbox" name="accesorios_alfombra_delantera" ${report.accesorios_alfombra_delantera ? "checked" : ""}> Alfombra Del</label>
                        <label><input type="checkbox" name="accesorios_alfombra_trasera" ${report.accesorios_alfombra_trasera ? "checked" : ""}> Alfombra Tras</label>
                        <label><input type="checkbox" name="accesorios_radio" ${report.accesorios_radio ? "checked" : ""}> Radio</label>
                        <label><input type="checkbox" name="accesorios_radio_reproductor" ${report.accesorios_radio_reproductor ? "checked" : ""}> Reproductor</label>
                        <label><input type="checkbox" name="accesorios_antena_electrica" ${report.accesorios_antena_electrica ? "checked" : ""}> Antena Eléc</label>
                        <label><input type="checkbox" name="accesorios_encendedor_cigarrillos" ${report.accesorios_encendedor_cigarrillos ? "checked" : ""}> Encendedor</label>
                        <label><input type="checkbox" name="accesorios_triangulo_seguridad" ${report.accesorios_triangulo_seguridad ? "checked" : ""}> Triángulo Seg</label>
                        <label><input type="checkbox" name="accesorios_gato" ${report.accesorios_gato ? "checked" : ""}> Gato</label>
                        <label><input type="checkbox" name="accesorios_caucho_repuesto" ${report.accesorios_caucho_repuesto ? "checked" : ""}> Caucho Rep</label>
                        <label><input type="checkbox" name="accesorios_otro" ${report.accesorios_otro ? "checked" : ""}> Otro</label>
                    </div>
                </div>

                <div class="form-section">
                    <h3>Checklist: Sistemas Eléctricos</h3>
                    <div class="checklist-form-grid">
                        <label><input type="checkbox" name="sistem_electric_frenos_del" ${report.sistem_electric_frenos_del ? "checked" : ""}> Frenos Del</label>
                        <label><input type="checkbox" name="sistem_electric_tablero" ${report.sistem_electric_tablero ? "checked" : ""}> Tablero</label>
                        <label><input type="checkbox" name="sistem_electric_luz_cruce" ${report.sistem_electric_luz_cruce ? "checked" : ""}> Luz Cruce</label>
                        <label><input type="checkbox" name="sistem_electric_stop" ${report.sistem_electric_stop ? "checked" : ""}> Luz Stop</label>
                        <label><input type="checkbox" name="sistem_electric_vidrio_electrico" ${report.sistem_electric_vidrio_electrico ? "checked" : ""}> Vidrio Eléc</label>
                        <label><input type="checkbox" name="sistem_electric_aire_acondicionado" ${report.sistem_electric_aire_acondicionado ? "checked" : ""}> Aire Acond</label>
                        <label><input type="checkbox" name="sistem_electric_otro" ${report.sistem_electric_otro ? "checked" : ""}> Otro</label>
                    </div>
                </div>

                <div class="form-section">
                    <h3>Observaciones Adicionales</h3>
                    <div class="form-full-width-item">
                        <textarea name="observaciones" placeholder="Anotar detalles extra sobre el checklist, golpes, rayones, etc.">${report.observaciones || ""}</textarea>
                    </div>
                </div>

                <div class="form-section">
                    <h3>Servicios</h3>
                    <div id="servicios-container"></div>
                    <button type="button" id="btnAddServicio" class="btn-add">+ Añadir Servicio</button>
                </div>

                <div class="form-section">
                    <h3>Repuestos</h3>
                    <div id="repuestos-container"></div>
                    <button type="button" id="btnAddRepuesto" class="btn-add">+ Añadir Repuesto</button>
                </div>

                <div class="form-actions">
                    <button type="button" id="btnCancelarEdicion">Cancelar</button>
                    <button type="submit">Actualizar Reporte</button>
                </div>
            </form>
        `;
    showContent(html);

    const serviciosContainer = document.getElementById("servicios-container");
    report.servicios.forEach((s, index) => {
      const i = index + 1;
      const div = document.createElement("div");
      div.className = "dynamic-item";
      div.innerHTML = `<input type="number" name="servicio_item_${i}" value="${s.item}" required><input type="text" name="servicio_desc_${i}" value="${s.descripcion}" required><input type="number" step="0.01" name="servicio_presupuesto_${i}" placeholder="Presupuesto" value="${s.presupuesto}" required><button type="button" class="btn-remove">X</button>`;
      serviciosContainer.appendChild(div);
      div.querySelector(".btn-remove").addEventListener("click", () => div.remove());
    });

    document.getElementById("btnAddServicio").addEventListener("click", () => {
      const i = serviciosContainer.children.length + 1;
      const div = document.createElement("div");
      div.className = "dynamic-item";
      div.innerHTML = `<input type="number" name="servicio_item_${i}" placeholder="Item" required value="${i}"><input type="text" name="servicio_desc_${i}" placeholder="Descripción" required><input type="number" step="0.01" name="servicio_presupuesto_${i}" placeholder="Presupuesto" required><button type="button" class="btn-remove">X</button>`;
      serviciosContainer.appendChild(div);
      div.querySelector(".btn-remove").addEventListener("click", () => div.remove());
    });

    const repuestosContainer = document.getElementById("repuestos-container");
    report.repuestos.forEach((r, index) => {
      const i = index + 1;
      const div = document.createElement("div");
      div.className = "dynamic-item";
      div.innerHTML = `<input type="number" name="repuesto_cant_${i}" value="${r.cantidad}" required><input type="text" name="repuesto_desc_${i}" value="${r.descripcion}" required><input type="number" step="0.01" name="repuesto_presupuesto_${i}" placeholder="Presupuesto" value="${r.presupuesto}" required><button type="button" class="btn-remove">X</button>`;
      repuestosContainer.appendChild(div);
      div.querySelector(".btn-remove").addEventListener("click", () => div.remove());
    });

    document.getElementById("btnAddRepuesto").addEventListener("click", () => {
      const i = repuestosContainer.children.length + 1;
      const div = document.createElement("div");
      div.className = "dynamic-item";
      div.innerHTML = `<input type="number" name="repuesto_cant_${i}" placeholder="Cantidad" required><input type="text" name="repuesto_desc_${i}" placeholder="Descripción" required><input type="number" step="0.01" name="repuesto_presupuesto_${i}" placeholder="Presupuesto" required><button type="button" class="btn-remove">X</button>`;
      repuestosContainer.appendChild(div);
      div.querySelector(".btn-remove").addEventListener("click", () => div.remove());
    });

    document.getElementById("btnCancelarEdicion").addEventListener("click", () => showReportDetails(report.id_reporte));

    document.getElementById("formEditReporte").addEventListener("submit", async (event) => {
      event.preventDefault();
      const formData = new FormData(event.target);

      const servicios = Array.from(serviciosContainer.children).map((div, index) => {
        const i = index + 1;
        return {
          item: parseInt(div.querySelector(`input[name^="servicio_item_"]`).value),
          descripcion: div.querySelector(`input[name^="servicio_desc_"]`).value,
          presupuesto: parseFloat(div.querySelector(`input[name^="servicio_presupuesto_"]`).value),
        };
      });

      const repuestos = Array.from(repuestosContainer.children).map((div, index) => {
        const i = index + 1;
        return {
          cantidad: parseInt(div.querySelector(`input[name^="repuesto_cant_"]`).value),
          descripcion: div.querySelector(`input[name^="repuesto_desc_"]`).value,
          presupuesto: parseFloat(div.querySelector(`input[name^="repuesto_presupuesto_"]`).value),
        };
      });

      const getOptionalFloat = (name) => {
        const value = formData.get(name);
        return value !== "" ? parseFloat(value) : null;
      };
      const getOptionalString = (name) => {
        const value = formData.get(name);
        return value !== "" ? value : null;
      };

      const updatedReporte = {
        id_reporte: report.id_reporte,
        fecha: report.fecha,
        placa: formData.get("placa"),
        modelo: formData.get("modelo"),
        color: formData.get("color"),
        nombre_cliente: formData.get("nombre_cliente"),
        cedula_cliente: parseInt(formData.get("cedula_cliente")),
        telefono_cliente: parseInt(formData.get("telefono_cliente")),
        status_reporte: formData.get("status_reporte"),
        factura_reporte: getOptionalString("factura_reporte"),
        factura_monto: getOptionalFloat("factura_monto"),
        // CARROCERÍA
        carroceria_golpe: formData.get("carroceria_golpe") === "on",
        carroceria_suelto: formData.get("carroceria_suelto") === "on",
        carroceria_rayas: formData.get("carroceria_rayas") === "on",
        carroceria_desconchado: formData.get("carroceria_desconchado") === "on",
        carroceria_vidrio_roto: formData.get("carroceria_vidrio_roto") === "on",
        carroceria_falta_moldura: formData.get("carroceria_falta_moldura") === "on",
        carroceria_falta_faro: formData.get("carroceria_falta_faro") === "on",
        carroceria_falta_accesorio: formData.get("carroceria_falta_accesorio") === "on",
        carroceria_espejo_roto: formData.get("carroceria_espejo_roto") === "on",
        carroceria_falta_centro_copas: formData.get("carroceria_falta_centro_copas") === "on",
        carroceria_otro: formData.get("carroceria_otro") === "on",
        // ACCESORIOS
        accesorios_alfombra_delantera: formData.get("accesorios_alfombra_delantera") === "on",
        accesorios_alfombra_trasera: formData.get("accesorios_alfombra_trasera") === "on",
        accesorios_radio: formData.get("accesorios_radio") === "on",
        accesorios_radio_reproductor: formData.get("accesorios_radio_reproductor") === "on",
        accesorios_antena_electrica: formData.get("accesorios_antena_electrica") === "on",
        accesorios_encendedor_cigarrillos: formData.get("accesorios_encendedor_cigarrillos") === "on",
        accesorios_triangulo_seguridad: formData.get("accesorios_triangulo_seguridad") === "on",
        accesorios_gato: formData.get("accesorios_gato") === "on",
        accesorios_caucho_repuesto: formData.get("accesorios_caucho_repuesto") === "on",
        accesorios_otro: formData.get("accesorios_otro") === "on",
        // SISTEMA ELECTRICO
        sistem_electric_frenos_del: formData.get("sistem_electric_frenos_del") === "on",
        sistem_electric_tablero: formData.get("sistem_electric_tablero") === "on",
        sistem_electric_luz_cruce: formData.get("sistem_electric_luz_cruce") === "on",
        sistem_electric_stop: formData.get("sistem_electric_stop") === "on",
        sistem_electric_vidrio_electrico: formData.get("sistem_electric_vidrio_electrico") === "on",
        sistem_electric_aire_acondicionado: formData.get("sistem_electric_aire_acondicionado") === "on",
        sistem_electric_otro: formData.get("sistem_electric_otro") === "on",

        observaciones: formData.get("observaciones"),
        servicios: servicios,
        repuestos: repuestos,
      };

      try {
        const response = await fetch(`/reportes/${report.id_reporte}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(updatedReporte),
        });
        if (response.ok) {
          const data = await response.json();
          alert("¡Reporte actualizado exitosamente!");
          showReportDetails(data.id_reporte);
        } else {
          const errorData = await response.json();
          alert(`Error al actualizar el reporte: ${errorData.detail}`);
        }
      } catch (error) {
        alert(`Error de red: ${error.message}`);
      }
    });
  };

  // --- Event Listeners para los botones del menú ---
  btnNuevoReporte.addEventListener("click", () => {
    // --- FUNCIÓN PARA RENDERIZAR EL FORMULARIO DE NUEVO REPORTE ---
    const renderNewReportForm = () => {
      let html = `
                <h2>Crear Nuevo Reporte</h2>
                <form id="formNuevoReporte" class="report-form">
                    <div class="form-section">
                        <h3>Datos del Cliente y Vehículo</h3>
                        <div class="form-grid">
                            <input type="text" name="placa" placeholder="Placa (ej: ABC12D)" required>
                            <input type="text" name="modelo" placeholder="Modelo del Vehículo" required>
                            <input type="text" name="color" placeholder="Color del Vehículo" required>
                            <input type="text" name="nombre_cliente" placeholder="Nombre del Cliente" required>
                            <input type="number" name="cedula_cliente" placeholder="Cédula del Cliente" required>
                            <input type="number" name="telefono_cliente" placeholder="Teléfono del Cliente" required>
                        </div>
                    </div>

                    <div class="form-section">
                        <h3>Datos de Facturación (Opcional)</h3>
                        <div class="form-grid">
                            <input type="text" name="factura_reporte" placeholder="Número de Factura (Opcional)">
                            <input type="number" step="0.01" name="factura_monto" placeholder="Monto de la Factura (Opcional)">
                        </div>
                    </div>

                    <div class="form-section">
                        <h3>Checklist: Carrocería</h3>
                        <div class="checklist-form-grid">
                            <label><input type="checkbox" name="carroceria_golpe"> Golpe</label>
                            <label><input type="checkbox" name="carroceria_suelto"> Suelto</label>
                            <label><input type="checkbox" name="carroceria_rayas"> Rayas</label>
                            <label><input type="checkbox" name="carroceria_desconchado"> Desconchado</label>
                            <label><input type="checkbox" name="carroceria_vidrio_roto"> Vidrio Roto</label>
                            <label><input type="checkbox" name="carroceria_falta_moldura"> Falta Moldura</label>
                            <label><input type="checkbox" name="carroceria_falta_faro"> Falta Faro</label>
                            <label><input type="checkbox" name="carroceria_falta_accesorio"> Falta Accesorio</label>
                            <label><input type="checkbox" name="carroceria_espejo_roto"> Espejo Roto</label>
                            <label><input type="checkbox" name="carroceria_falta_centro_copas"> Falta Centro Copas</label>
                            <label><input type="checkbox" name="carroceria_otro"> Otro</label>
                        </div>
                    </div>

                    <div class="form-section">
                        <h3>Checklist: Accesorios</h3>
                        <div class="checklist-form-grid">
                            <label><input type="checkbox" name="accesorios_alfombra_delantera"> Alfombra Del</label>
                            <label><input type="checkbox" name="accesorios_alfombra_trasera"> Alfombra Tras</label>
                            <label><input type="checkbox" name="accesorios_radio"> Radio</label>
                            <label><input type="checkbox" name="accesorios_radio_reproductor"> Reproductor</label>
                            <label><input type="checkbox" name="accesorios_antena_electrica"> Antena Eléc</label>
                            <label><input type="checkbox" name="accesorios_encendedor_cigarrillos"> Encendedor</label>
                            <label><input type="checkbox" name="accesorios_triangulo_seguridad"> Triángulo Seg</label>
                            <label><input type="checkbox" name="accesorios_gato"> Gato</label>
                            <label><input type="checkbox" name="accesorios_caucho_repuesto"> Caucho Rep</label>
                            <label><input type="checkbox" name="accesorios_otro"> Otro</label>
                        </div>
                    </div>

                    <div class="form-section">
                        <h3>Checklist: Sistemas Eléctricos</h3>
                        <div class="checklist-form-grid">
                            <label><input type="checkbox" name="sistem_electric_frenos_del"> Frenos Del</label>
                            <label><input type="checkbox" name="sistem_electric_tablero"> Tablero</label>
                            <label><input type="checkbox" name="sistem_electric_luz_cruce"> Luz Cruce</label>
                            <label><input type="checkbox" name="sistem_electric_stop"> Luz Stop</label>
                            <label><input type="checkbox" name="sistem_electric_vidrio_electrico"> Vidrio Eléc</label>
                            <label><input type="checkbox" name="sistem_electric_aire_acondicionado"> Aire Acond</label>
                            <label><input type="checkbox" name="sistem_electric_otro"> Otro</label>
                        </div>
                    </div>

                    <div class="form-section">
                        <h3>Observaciones Adicionales</h3>
                        <div class="form-full-width-item">
                            <textarea name="observaciones" placeholder="Anotar detalles extra sobre el checklist, golpes, rayones, etc."></textarea>
                        </div>
                    </div>

                    <div class="form-section">
                        <h3>Servicios a Realizar</h3>
                        <div id="servicios-container"></div>
                        <button type="button" id="btnAddServicio" class="btn-add">+ Añadir Servicio</button>
                    </div>

                    <div class="form-section">
                        <h3>Repuestos a Utilizar</h3>
                        <div id="repuestos-container"></div>
                        <button type="button" id="btnAddRepuesto" class="btn-add">+ Añadir Repuesto</button>
                    </div>

                    <div class="form-actions">
                        <button type="submit">Guardar Reporte</button>
                    </div>
                </form>
            `;
      showContent(html);

      document.getElementById("btnAddServicio").addEventListener("click", () => {
        const i = document.getElementById("servicios-container").children.length + 1;
        const div = document.createElement("div");
        div.className = "dynamic-item";
        div.innerHTML = `<input type="number" name="servicio_item_${i}" placeholder="Item" required value="${i}"><input type="text" name="servicio_desc_${i}" placeholder="Descripción del Servicio" required><input type="number" step="0.01" name="servicio_presupuesto_${i}" placeholder="Presupuesto" required><button type="button" class="btn-remove">X</button>`;
        document.getElementById("servicios-container").appendChild(div);
        div.querySelector(".btn-remove").addEventListener("click", () => div.remove());
      });

      document.getElementById("btnAddRepuesto").addEventListener("click", () => {
        const i = document.getElementById("repuestos-container").children.length + 1;
        const div = document.createElement("div");
        div.className = "dynamic-item";
        div.innerHTML = `<input type="number" name="repuesto_cant_${i}" placeholder="Cantidad" required><input type="text" name="repuesto_desc_${i}" placeholder="Descripción del Repuesto" required><input type="number" step="0.01" name="repuesto_presupuesto_${i}" placeholder="Presupuesto" required><button type="button" class="btn-remove">X</button>`;
        document.getElementById("repuestos-container").appendChild(div);
        div.querySelector(".btn-remove").addEventListener("click", () => div.remove());
      });

      document.getElementById("formNuevoReporte").addEventListener("submit", async (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);

        const servicios = Array.from(document.getElementById("servicios-container").children).map((div, index) => {
          const i = index + 1;
          return {
            item: parseInt(div.querySelector(`input[name^="servicio_item_"]`).value),
            descripcion: div.querySelector(`input[name^="servicio_desc_"]`).value,
            presupuesto: parseFloat(div.querySelector(`input[name^="servicio_presupuesto_"]`).value),
          };
        });

        const repuestos = Array.from(document.getElementById("repuestos-container").children).map((div, index) => {
          const i = index + 1;
          return {
            cantidad: parseInt(div.querySelector(`input[name^="repuesto_cant_"]`).value),
            descripcion: div.querySelector(`input[name^="repuesto_desc_"]`).value,
            presupuesto: parseFloat(div.querySelector(`input[name^="repuesto_presupuesto_"]`).value),
          };
        });

        const getOptionalNumber = (name) => {
          const value = formData.get(name);
          return value !== "" ? parseFloat(value) : null;
        };
        const getOptionalString = (name) => {
          const value = formData.get(name);
          return value !== "" ? value : null;
        };
        const reporte = {
          placa: formData.get("placa"),
          modelo: formData.get("modelo"),
          color: formData.get("color"),
          nombre_cliente: formData.get("nombre_cliente"),
          cedula_cliente: parseInt(formData.get("cedula_cliente")),
          telefono_cliente: parseInt(formData.get("telefono_cliente")),
          factura_reporte: getOptionalString("factura_reporte"),
          factura_monto: getOptionalNumber("factura_monto"),
          // CARROCERÍA
          carroceria_golpe: formData.get("carroceria_golpe") === "on",
          carroceria_suelto: formData.get("carroceria_suelto") === "on",
          carroceria_rayas: formData.get("carroceria_rayas") === "on",
          carroceria_desconchado: formData.get("carroceria_desconchado") === "on",
          carroceria_vidrio_roto: formData.get("carroceria_vidrio_roto") === "on",
          carroceria_falta_moldura: formData.get("carroceria_falta_moldura") === "on",
          carroceria_falta_faro: formData.get("carroceria_falta_faro") === "on",
          carroceria_falta_accesorio: formData.get("carroceria_falta_accesorio") === "on",
          carroceria_espejo_roto: formData.get("carroceria_espejo_roto") === "on",
          carroceria_falta_centro_copas: formData.get("carroceria_falta_centro_copas") === "on",
          carroceria_otro: formData.get("carroceria_otro") === "on",
          // ACCESORIOS
          accesorios_alfombra_delantera: formData.get("accesorios_alfombra_delantera") === "on",
          accesorios_alfombra_trasera: formData.get("accesorios_alfombra_trasera") === "on",
          accesorios_radio: formData.get("accesorios_radio") === "on",
          accesorios_radio_reproductor: formData.get("accesorios_radio_reproductor") === "on",
          accesorios_antena_electrica: formData.get("accesorios_antena_electrica") === "on",
          accesorios_encendedor_cigarrillos: formData.get("accesorios_encendedor_cigarrillos") === "on",
          accesorios_triangulo_seguridad: formData.get("accesorios_triangulo_seguridad") === "on",
          accesorios_gato: formData.get("accesorios_gato") === "on",
          accesorios_caucho_repuesto: formData.get("accesorios_caucho_repuesto") === "on",
          accesorios_otro: formData.get("accesorios_otro") === "on",
          // SISTEMA ELECTRICO
          sistem_electric_frenos_del: formData.get("sistem_electric_frenos_del") === "on",
          sistem_electric_tablero: formData.get("sistem_electric_tablero") === "on",
          sistem_electric_luz_cruce: formData.get("sistem_electric_luz_cruce") === "on",
          sistem_electric_stop: formData.get("sistem_electric_stop") === "on",
          sistem_electric_vidrio_electrico: formData.get("sistem_electric_vidrio_electrico") === "on",
          sistem_electric_aire_acondicionado: formData.get("sistem_electric_aire_acondicionado") === "on",
          sistem_electric_otro: formData.get("sistem_electric_otro") === "on",

          observaciones: formData.get("observaciones"),
          servicios: servicios,
          repuestos: repuestos,
        };
        try {
          const response = await fetch("/reportes/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(reporte),
          });
          const data = await response.json();
          if (response.ok) {
            alert("¡Reporte creado exitosamente!");
            showReportDetails(data.id_reporte);
          } else {
            alert(`Error al crear el reporte: ${data.detail}`);
          }
        } catch (error) {
          alert(`Error de red: ${error.message}`);
        }
      });
    };
    renderNewReportForm();
  });

  btnConsultarReporte.addEventListener("click", () => {
    let html = `
            <h2>Consultar Reporte por ID</h2>
            <div class="form-container">
                <input type="text" id="reporteIdInput" placeholder="Introduce el ID del reporte" />
                <button id="btnBuscarReporte">Buscar</button>
            </div>
        `;
    showContent(html);
    document.getElementById("btnBuscarReporte").addEventListener("click", async () => {
      const reporteId = document.getElementById("reporteIdInput").value;
      if (!reporteId) {
        showContent('<p class="error-message">Por favor, introduce un ID de reporte.</p>');
        return;
      }
      showReportDetails(reporteId);
    });
  });

  btnConsultarCliente.addEventListener("click", () => {
    let html = `
            <h2>Consultar Reportes por Cédula de Cliente</h2>
            <div class="form-container">
                <input type="text" id="cedulaClienteInput" placeholder="Introduce la cédula del cliente" />
                <button id="btnBuscarCliente">Buscar</button>
            </div>
        `;
    showContent(html);
    document.getElementById("btnBuscarCliente").addEventListener("click", async () => {
      const cedulaCliente = document.getElementById("cedulaClienteInput").value;
      if (!cedulaCliente) {
        showContent('<p class="error-message">Por favor, introduce una cédula.</p>');
        return;
      }
      showContent(`<p>Cargando reportes para la cédula: ${cedulaCliente}...</p>`);
      try {
        const response = await fetch(`/reportes/cliente/${cedulaCliente}`);
        const data = await response.json();
        if (response.ok) {
          renderReportList(data);
        } else {
          showContent(
            `<p class="error-message">Error: ${data.detail || "No se encontraron reportes para esta cédula."}</p>`,
          );
        }
      } catch (error) {
        showContent(`<p class="error-message">Error de red: ${error.message}`);
      }
    });
  });

  btnListaReportes.addEventListener("click", async () => {
    showContent("<p>Cargando lista de reportes...</p>");
    try {
      const response = await fetch("/reportes/");
      const data = await response.json();
      if (response.ok) {
        renderReportList(data);
      } else {
        showContent(`<p>Error al cargar reportes: ${data.detail}</p>`);
      }
    } catch (error) {
      showContent(`<p>Error de red: ${error.message}`);
    }
  });
});