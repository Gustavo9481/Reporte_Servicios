import { BaseComponent } from "../BaseComponent.js";

const styles = `
    :host {
        display: inline-block;
        min-width: 140px;
    }
    button {
        background-color: var(--green-color, #2a9d8f);
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
        background-color: var(--darker-green, #217d72);
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

        // Propagate the 'type' attribute to the inner button
        if (this.hasAttribute('type')) {
            this.shadowRoot.querySelector('button').type = this.getAttribute('type');
        }

        // Propagate clicks from the button to the custom element
        this.shadowRoot.querySelector('button').addEventListener('click', (event) => {
            // If the inner button is a submit button, we need to find the form and submit it.
            if (this.shadowRoot.querySelector('button').type === 'submit') {
                const form = this.closest('form');
                if (form) {
                    // Create a temporary submit button and click it to trigger the form's submit event
                    const tempSubmit = document.createElement('button');
                    tempSubmit.type = 'submit';
                    tempSubmit.style.display = 'none';
                    form.appendChild(tempSubmit);
                    tempSubmit.click();
                    form.removeChild(tempSubmit);
                    return; // Stop further event propagation
                }
            }
            
            // For non-submit clicks, dispatch a simple click event
            this.dispatchEvent(new MouseEvent('click', {
                bubbles: true,
                composed: true,
            }));
        });
    }
}

customElements.define('app-button-green', AppButtonGreen);
