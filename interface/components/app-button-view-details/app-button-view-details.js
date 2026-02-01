import { BaseComponent } from "../BaseComponent.js";

const styles = `
    :host {
        display: inline-block;
    }
    button {
        background-color: var(--green-color, #2a9d8f);
        color: var(--white-color, white);
        padding: 5px 10px; /* Tamaño pequeño */
        border: none; /* Sin borde */
        border-radius: 5px; /* Redondeado */
        cursor: pointer;
        font-size: 13px; /* Tamaño de fuente pequeño */
        transition: background-color 0.3s ease; /* Animación de hover */
        box-sizing: border-box;
        min-width: unset; /* Eliminar min-width por defecto si no es necesario */
    }

    button:hover {
        background-color: var(--darker-green, #217d72);
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

        // Propagate clicks from the button to the custom element
        this.shadowRoot.querySelector('button').addEventListener('click', (event) => {
            this.dispatchEvent(new MouseEvent('click', {
                bubbles: true,
                composed: true,
            }));
        });
    }
}

customElements.define('app-button-view-details', AppButtonViewDetails);
