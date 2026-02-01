import { BaseComponent } from "../BaseComponent.js";

const styles = `
    :host {
        display: inline-block;
        min-width: 140px;
    }
    button {
        background-color: var(--blue-color, #4361ee);
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
        background-color: var(--darker-blue, #3a56d4);
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

        // Propagate clicks from the button to the custom element
        this.shadowRoot.querySelector('button').addEventListener('click', (event) => {
            // Re-dispatch the event from the custom element
            this.dispatchEvent(new MouseEvent('click', {
                bubbles: true,
                composed: true,
            }));
        });
    }
}

customElements.define('app-button-blue', AppButtonBlue);
