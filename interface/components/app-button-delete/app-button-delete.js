import { BaseComponent } from "../BaseComponent.js";

const styles = `
    :host {
        display: inline-flex; /* Usar inline-flex para centrar contenido */
        align-items: center;
        justify-content: center;
        width: 90px; /* Tamaño un poco más grande para un botón */
        height: 30px; /* Tamaño un poco más grande para un botón */
        border-radius: 50%;
        background-color: var(--red-color, #c1121f); /* Color rojo para eliminar */
        color: var(--white-color, white);
        font-size: 16px; /* Tamaño de fuente para la 'X' */
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
                <slot></slot>
            </button>
        `;

    // Propagate clicks from the button to the custom element
    this.shadowRoot.querySelector("button").addEventListener("click", (event) => {
      // Re-dispatch the event from the custom element
      this.dispatchEvent(
        new MouseEvent("click", {
          bubbles: true,
          composed: true,
        }),
      );
    });
  }
}

customElements.define("app-button-delete", AppButtonDelete);
