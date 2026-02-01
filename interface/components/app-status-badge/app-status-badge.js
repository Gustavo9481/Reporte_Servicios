import { BaseComponent } from "../BaseComponent.js";

class AppStatusBadge extends BaseComponent {
    constructor() {
        super();
        this._status = this.getAttribute('status') || 'activa';
    }

    static get observedAttributes() {
        return ['status'];
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (name === 'status' && oldValue !== newValue) {
            this._status = newValue;
            this.render();
        }
    }

    connectedCallback() {
        this.render();
    }

    render() {
        const isActiva = this._status === 'activa';
        const backgroundColor = isActiva ? 'var(--green-color, #2a9d8f)' : 'var(--red-color, #c1121f)';
        const textColor = 'var(--white-color, white)';
        const textContent = isActiva ? '✔' : '✖';
        const titleText = isActiva ? 'Activa' : 'Anulada';

        // Los estilos ahora se calculan dinámicamente y se aplican
        const styles = `
            :host {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                width: 24px;
                height: 24px;
                border-radius: 50%;
                background-color: ${backgroundColor};
                color: ${textColor};
                font-size: 14px;
                font-weight: bold;
                border: none;
                box-shadow: 0 1px 3px rgba(0,0,0,0.2);
                cursor: default;
                margin: 0;
            }
        `;
        
        // Limpiamos el shadow root y aplicamos todo de nuevo para asegurar la actualización
        this.shadowRoot.innerHTML = '';
        this.applyStyles(styles);
        this.shadowRoot.innerHTML += `<span title="${titleText}">${textContent}</span>`;
    }
}

customElements.define('app-status-badge', AppStatusBadge);
