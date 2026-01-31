// interface/components/app-button-blue/app-button-blue.js

class AppButtonBlue extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.render();
    }

    render() {
        this.shadowRoot.innerHTML = `
            <style>
                button {
                    background-color: var(--blue-color, #4361ee);
                    color: var(--white-color, white);
                    padding: 10px 15px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 14px;
                    transition: background-color 0.3s ease;
                }

                button:hover {
                    background-color: var(--darker-blue, #3a56d4);
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

customElements.define('app-button-blue', AppButtonBlue);
