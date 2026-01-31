// interface/components/app-status-badge/app-status-badge.js

class AppStatusBadge extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this._status = 'activa'; // Valor por defecto
    }

    // Define qué atributos deben ser observados para cambios
    static get observedAttributes() {
        return ['status'];
    }

    // Se llama cuando un atributo observado cambia, se añade o se elimina
    attributeChangedCallback(name, oldValue, newValue) {
        if (name === 'status' && oldValue !== newValue) {
            this._status = newValue;
            this.render();
        }
    }

    connectedCallback() {
        // Asegurarse de que el renderizado inicial ocurra si el atributo ya está presente
        if (this.hasAttribute('status')) {
            this._status = this.getAttribute('status');
        }
        this.render();
    }

    render() {
        const isActiva = this._status === 'activa';
        const backgroundColor = isActiva ? 'var(--green-color, #2a9d8f)' : 'var(--red-color, #c1121f)';
        const textColor = 'var(--white-color, white)';
        const textContent = isActiva ? '✔' : '✖';
        const titleText = isActiva ? 'Activa' : 'Anulada';

        this.shadowRoot.innerHTML = `
            <style>
                :host {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    width: 24px; /* Pequeño */
                    height: 24px; /* Pequeño */
                    border-radius: 50%; /* Circular */
                    background-color: ${backgroundColor};
                    color: ${textColor};
                    font-size: 14px;
                    font-weight: bold;
                    border: none; /* Sin bordes */
                    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
                    cursor: default;
                    margin: 0; /* Asegurar que no haya márgenes externos */
                }
            </style>
            <span title="${titleText}">${textContent}</span>
        `;
    }
}

customElements.define('app-status-badge', AppStatusBadge);
