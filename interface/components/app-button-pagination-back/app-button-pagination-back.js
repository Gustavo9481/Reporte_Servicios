import { BaseComponent } from "../BaseComponent";

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

class AppButtonPaginationBack extends BaseComponent {
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

    this.shadowRoot.querySelector("button").addEventListener("click", () => {
      this.dispatchEvent(new CustomEvent("pagination-back"));
    });
  }
}

customElements.define("app-button-pagination-back", AppButtonPaginationBack);
