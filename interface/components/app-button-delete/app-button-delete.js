// MODULO: interface/components/app-button-delete/app-button-delete.js

// Web Component para botón eliminar servicio o repuesto (x).

import { BaseComponent } from "../BaseComponent.js";

const styles = `
    :host {
        display: inline-flex; /* Usar inline-flex para centrar contenido */
        align-items: center;
        justify-content: center;
        width: 24px; /* Tamaño ajustado para igualar a app-status-badge */
        height: 24px; /* Tamaño ajustado para igualar a app-status-badge */
        border-radius: 50%;
        background-color: var(--red-color, #c1121f); /* Color rojo para eliminar */
        color: var(--white-color, white);
        font-size: 14px; /* Tamaño de fuente ajustado */
        font-weight: bold;
        border: none;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        cursor: pointer; /* Indicar que es interactivo */
        margin: 0 5px; /* Espacio alrededor del botón */
        transition: background-color 0.3s ease; /* Transición para hover */
    }
    :host(:hover) {
        background-color: var(--darker-red, #9a0e19); /* Oscurecer en hover */
    }
    button {
        background: none; /* El background lo maneja :host */
        border: none;
        color: inherit; /* Heredar color del host */
        font: inherit; /* Heredar fuente del host */
        cursor: inherit; /* Heredar cursor del host */
        padding: 0;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
`;

class AppButtonDelete extends BaseComponent {
  constructor() {
    super();
  }

  connectedCallback() {
    this.applyStyles(styles);
    this.shadowRoot.innerHTML += `
            <button>
                <slot>✖</slot>
            </button>
        `;

    this.setupSubmitBehavior(this.shadowRoot.querySelector("button"));
  }
}

customElements.define("app-button-delete", AppButtonDelete);
