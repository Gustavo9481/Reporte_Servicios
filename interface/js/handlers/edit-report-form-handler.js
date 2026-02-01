// MÓDULO: interface/js/handlers/edit-report-form-handler.js
import { showContent } from "../utils/dom-utils.js";
import { showReportDetails } from "./report-details-handler.js";

const contentArea = document.getElementById("contentArea");

export const renderEditReportForm = (report) => {
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
                    <h3>Carrocería</h3>
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
                    <h3>Accesorios</h3>
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
                    <h3>Sistemas Eléctricos</h3>
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
                    <app-button-blue id="btnAddServicio">+ Añadir Servicio</app-button-blue>
                </div>

                <div class="form-section">
                    <h3>Repuestos</h3>
                    <div id="repuestos-container"></div>
                    <app-button-blue id="btnAddRepuesto">+ Añadir Repuesto</app-button-blue>
                </div>

                <div class="form-actions" style="display: flex; gap: 10px; justify-content: flex-end;">
                    <app-button-red id="btnCancelarEdicion">Cancelar</app-button-red>
                    <app-button-green type="submit">Actualizar Reporte</app-button-green>
                </div>
            </form>
        `;
  showContent(contentArea, html);

  const serviciosContainer = document.getElementById("servicios-container");
  report.servicios.forEach((s, index) => {
    const i = index + 1;
    const div = document.createElement("div");
    div.className = "dynamic-item";
            div.innerHTML = `<input type="number" name="servicio_item_${i}" value="${s.item}" required><input type="text" name="servicio_desc_${i}" value="${s.descripcion}" required><input type="number" step="0.01" name="servicio_presupuesto_${i}" placeholder="Presupuesto" value="${s.presupuesto}" required><app-button-red class="btn-remove">X</app-button-red>`;      serviciosContainer.appendChild(div);
    div.querySelector(".btn-remove").addEventListener("click", () => div.remove());
  });

  document.getElementById("btnAddServicio").addEventListener("click", () => {
    const i = serviciosContainer.children.length + 1;
    const div = document.createElement("div");
    div.className = "dynamic-item";
    div.innerHTML = `<input type="number" name="servicio_item_${i}" placeholder="Item" required value="${i}"><input type="text" name="servicio_desc_${i}" placeholder="Descripción" required><input type="number" step="0.01" name="servicio_presupuesto_${i}" placeholder="Presupuesto" required><app-button-red class="btn-remove">X</app-button-red>`;
    serviciosContainer.appendChild(div);
    div.querySelector(".btn-remove").addEventListener("click", () => div.remove());
  });

  const repuestosContainer = document.getElementById("repuestos-container");
  report.repuestos.forEach((r, index) => {
    const i = index + 1;
    const div = document.createElement("div");
    div.className = "dynamic-item";
            div.innerHTML = `<input type="number" name="repuesto_cant_${i}" value="${r.cantidad}" required><input type="text" name="repuesto_desc_${i}" value="${r.descripcion}" required><input type="number" step="0.01" name="repuesto_presupuesto_${i}" placeholder="Presupuesto" value="${r.presupuesto}" required><app-button-red class="btn-remove">X</app-button-red>`;      repuestosContainer.appendChild(div);
    div.querySelector(".btn-remove").addEventListener("click", () => div.remove());
  });

  document.getElementById("btnAddRepuesto").addEventListener("click", () => {
    const i = repuestosContainer.children.length + 1;
    const div = document.createElement("div");
    div.className = "dynamic-item";
    div.innerHTML = `<input type="number" name="repuesto_cant_${i}" placeholder="Cantidad" required><input type="text" name="repuesto_desc_${i}" placeholder="Descripción" required><input type="number" step="0.01" name="repuesto_presupuesto_${i}" placeholder="Presupuesto" required><app-button-red class="btn-remove">X</app-button-red>`;
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
