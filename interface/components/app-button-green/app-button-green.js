// MODULO: interface/components/app-button-green/app-button-green.js

// Componente personalizado para un botón verde rectangular.

import { BaseComponent } from "../BaseComponent.js";

const styles = `
    :host {
        display: inline-block;
        min-width: 140px;
    }
    button {
        background-color: var(--green-color);
        color: var(--white-color, white);
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 14px;
        transition: background-color 0.3s ease;
        width: 100%;
        box-sizing: border-box;
    }

    button:hover {
        background-color: var(--green-darker);
    }
`;

class AppButtonGreen extends BaseComponent {
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

    this.setupSubmitBehavior(this.shadowRoot.querySelector("button"));
  }
}

customElements.define("app-button-green", AppButtonGreen);
