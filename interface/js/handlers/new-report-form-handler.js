// MÓDULO: interface/js/handlers/new-report-form-handler.js
import { showContent } from "../utils/dom-utils.js";
import { showReportDetails } from "./report-details-handler.js";
import { renderReportList } from "./report-list-handler.js";

const contentArea = document.getElementById("contentArea");

export const renderNewReportForm = () => {
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
                        <h3>Carrocería</h3>
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
                        <h3>Accesorios</h3>
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
                        <h3>Sistemas Eléctricos</h3>
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
                        <app-button-blue id="btnAddServicio">+ Añadir Servicio</app-button-blue>
                    </div>

                    <div class="form-section">
                        <h3>Repuestos a Utilizar</h3>
                        <div id="repuestos-container"></div>
                        <app-button-blue id="btnAddRepuesto">+ Añadir Repuesto</app-button-blue>
                    </div>

                    <div class="form-actions" style="display: flex; gap: 10px; justify-content: flex-end;">
                        <app-button-red id="btnCancelarNuevoReporte">Cancelar</app-button-red>
                        <app-button-green type="submit">Guardar Reporte</app-button-green>
                    </div>
                </form>
            `;
    showContent(contentArea, html);

    document.getElementById("btnAddServicio").addEventListener("click", () => {
      const i = document.getElementById("servicios-container").children.length + 1;
      const div = document.createElement("div");
      div.className = "dynamic-item";
      div.innerHTML = `<input type="number" name="servicio_item_${i}" placeholder="Item" required value="${i}"><input type="text" name="servicio_desc_${i}" placeholder="Descripción del Servicio" required><input type="number" step="0.01" name="servicio_presupuesto_${i}" placeholder="Presupuesto" required><app-button-delete class="btn-remove">X</app-button-delete>`;
      document.getElementById("servicios-container").appendChild(div);
      div.querySelector(".btn-remove").addEventListener("click", () => div.remove());
    });

    document.getElementById("btnAddRepuesto").addEventListener("click", () => {
      const i = document.getElementById("repuestos-container").children.length + 1;
      const div = document.createElement("div");
      div.className = "dynamic-item";
      div.innerHTML = `<input type="number" name="repuesto_cant_${i}" placeholder="Cantidad" required><input type="text" name="repuesto_desc_${i}" placeholder="Descripción del Repuesto" required><input type="number" step="0.01" name="repuesto_presupuesto_${i}" placeholder="Presupuesto" required><app-button-delete class="btn-remove">X</app-button-delete>`;
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
          alert(`Error al crear el reporte: ${data.detail || "Error desconocido"}`); // Añadido detalle de error
        }
      } catch (error) {
        alert(`Error de red: ${error.message}`);
      }
    });

    document.getElementById("btnCancelarNuevoReporte").addEventListener("click", () => {
        showContent(contentArea, ""); // Limpia el área de contenido
        // Aquí podrías querer volver a la lista de reportes, si tiene sentido en el flujo
        renderReportList(); // Asumimos que podemos recargar la lista de reportes
    });
  };
