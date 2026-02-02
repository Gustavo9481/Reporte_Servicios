import { BaseComponent } from "../BaseComponent.js";

const styles = `
    :host {
      display: inline-block;
    }
    button {
      background-color: #4361ee;
      color: white;
      border: none;
      border-radius: 50%; /* Makes it a circle */
      cursor: pointer;
      transition: background-color 0.3s ease;
      width: 40px; /* Fixed width */
      height: 40px; /* Fixed height */
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2em;
      line-height: 1;
    }
    button:hover {
      background-color: #3a56d4; /* Darker blue */
    }
    button:disabled {
      background-color: #ccc;
      color: #666;
      cursor: not-allowed;
    }
`;

class AppButtonPaginationNext extends BaseComponent {
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

customElements.define('app-button-pagination-next', AppButtonPaginationNext);
