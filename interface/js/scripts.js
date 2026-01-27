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

                        <h3>Checklist del Vehículo</h3>
                        <table class="details-table checklist-table">
                            <tr>
                                <td class="${data.carroceria_golpe ? "check-true" : "check-false"}">Golpes en Carrocería ${data.carroceria_golpe ? "<strong>(X)</strong>" : ""}</td>
                                <td class="${data.carroceria_vidrio_roto ? "check-true" : "check-false"}">Vidrios Rotos ${data.carroceria_vidrio_roto ? "<strong>(X)</strong>" : ""}</td>
                            </tr>
                            <tr>
                                <td class="${data.accesorios_alfombra ? "check-true" : "check-false"}">Alfombras ${data.accesorios_alfombra ? "<strong>(X)</strong>" : ""}</td>
                                <td class="${data.accesorios_radio ? "check-true" : "check-false"}">Radio ${data.accesorios_radio ? "<strong>(X)</strong>" : ""}</td>
                            </tr>
                            <tr>
                                <td class="${data.sistem_electric_frenos_del ? "check-true" : "check-false"}">Frenos Delanteros ${data.sistem_electric_frenos_del ? "<strong>(X)</strong>" : ""}</td>
                                <td class="${data.sistem_electric_tablero ? "check-true" : "check-false"}">Tablero Eléctrico ${data.sistem_electric_tablero ? "<strong>(X)</strong>" : ""}</td>
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
                    <h3>Checklist de Ingreso</h3>
                    <div class="checklist-form-grid">
                        <label><input type="checkbox" name="carroceria_golpe" ${report.carroceria_golpe ? "checked" : ""}> Golpes</label>
                        <label><input type="checkbox" name="carroceria_vidrio_roto" ${report.carroceria_vidrio_roto ? "checked" : ""}> Vidrios Rotos</label>
                        <label><input type="checkbox" name="accesorios_alfombra" ${report.accesorios_alfombra ? "checked" : ""}> Alfombras</label>
                        <label><input type="checkbox" name="accesorios_radio" ${report.accesorios_radio ? "checked" : ""}> Radio</label>
                        <label><input type="checkbox" name="sistem_electric_frenos_del" ${report.sistem_electric_frenos_del ? "checked" : ""}> Frenos Del.</label>
                        <label><input type="checkbox" name="sistem_electric_tablero" ${report.sistem_electric_tablero ? "checked" : ""}> Tablero</label>
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
        carroceria_golpe: formData.get("carroceria_golpe") === "on",
        carroceria_vidrio_roto: formData.get("carroceria_vidrio_roto") === "on",
        accesorios_alfombra: formData.get("accesorios_alfombra") === "on",
        accesorios_radio: formData.get("accesorios_radio") === "on",
        sistem_electric_frenos_del: formData.get("sistem_electric_frenos_del") === "on",
        sistem_electric_tablero: formData.get("sistem_electric_tablero") === "on",
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
                        <h3>Checklist de Ingreso</h3>
                        <div class="checklist-form-grid">
                            <label><input type="checkbox" name="carroceria_golpe"> Golpes en Carrocería</label>
                            <label><input type="checkbox" name="carroceria_vidrio_roto"> Vidrios Rotos</label>
                            <label><input type="checkbox" name="accesorios_alfombra"> Alfombras</label>
                            <label><input type="checkbox" name="accesorios_radio"> Radio</label>
                            <label><input type="checkbox" name="sistem_electric_frenos_del"> Frenos Delanteros</label>
                            <label><input type="checkbox" name="sistem_electric_tablero"> Tablero Eléctrico</label>
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
          carroceria_golpe: formData.get("carroceria_golpe") === "on",
          carroceria_vidrio_roto: formData.get("carroceria_vidrio_roto") === "on",
          accesorios_alfombra: formData.get("accesorios_alfombra") === "on",
          accesorios_radio: formData.get("accesorios_radio") === "on",
          sistem_electric_frenos_del: formData.get("sistem_electric_frenos_del") === "on",
          sistem_electric_tablero: formData.get("sistem_electric_tablero") === "on",
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
