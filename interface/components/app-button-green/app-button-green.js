// interface/components/app-button-green/app-button-green.js

class AppButtonGreen extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.render();
    }

    render() {
        this.shadowRoot.innerHTML = `
            <style>
                button {
                    background-color: var(--green-color, #2a9d8f);
                    color: var(--white-color, white);
                    padding: 10px 15px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 14px;
                    transition: background-color 0.3s ease;
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

customElements.define('app-button-green', AppButtonGreen);
