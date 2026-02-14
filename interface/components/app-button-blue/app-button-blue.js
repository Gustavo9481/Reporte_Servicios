// MODULO: interface/components/app-button-blue/app-button-blue.js

// Componente personalizado para botones azules rectangilares.

import { BaseComponent } from "../BaseComponent.js";

const styles = `
    :host {
        display: inline-block;
        min-width: 140px;
    }
    button {
        background-color: var(--blue-color);
        color: var(--white-color);
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
        background-color: var(--blue-darker);
    }
`;

class AppButtonBlue extends BaseComponent {
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

customElements.define("app-button-blue", AppButtonBlue);
