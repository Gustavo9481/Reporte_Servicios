// interface/components/app-button-view-details/app-button-view-details.js

class AppButtonViewDetails extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.render();
    }

    render() {
        this.shadowRoot.innerHTML = `
            <style>
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
            </style>
            <button>
                <slot></slot>
            </button>
        `;

        this.shadowRoot.querySelector('button').addEventListener('click', (event) => {
            this.dispatchEvent(new CustomEvent('click', {
                bubbles: true,
                composed: true,
                detail: event
            }));
        });
    }
}

customElements.define('app-button-view-details', AppButtonViewDetails);
