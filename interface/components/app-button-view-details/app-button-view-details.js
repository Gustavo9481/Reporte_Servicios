// MÓDULO: interface/components/app-button-view-details/app-button-view-details.js
//.. ................................................. AppButtonViewDetails ..
// Componente personalizado para boton de Ver Detalles de reportes.

import { BaseComponent } from "../BaseComponent.js";

const styles = `
    :host {
        display: inline-block;
    }
    button {
        background-color: var(--green-color);
        color: var(--white-color);
        padding: 5px 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 13px;
        transition: background-color 0.3s ease;
        box-sizing: border-box;
        min-width: unset;
    }

    button:hover {
        background-color: var(--green-darker);
    }
`;

class AppButtonViewDetails extends BaseComponent {
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

customElements.define("app-button-view-details", AppButtonViewDetails);
