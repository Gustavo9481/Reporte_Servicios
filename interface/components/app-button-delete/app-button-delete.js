// MODULO: interface/components/app-button-delete/app-button-delete.js

// Web Component para botón eliminar servicio o repuesto (x).

import { BaseComponent } from "../BaseComponent.js";

const styles = `
    :host {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        height: 24px;
        border-radius: 50%;
        background-color: var(--red-color);
        color: var(--white-color);
        font-size: 14px;
        font-weight: bold;
        border: none;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        cursor: pointer;
        margin: 0 5px;
        transition: background-color 0.3s ease;
    }
    :host(:hover) {
        background-color: var(--red-darker);
    }
    button {
        background: none;
        border: none;
        color: inherit;
        font: inherit;
        cursor: inherit;
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
