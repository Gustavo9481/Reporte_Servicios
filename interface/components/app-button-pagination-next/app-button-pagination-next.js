import { BaseComponent } from "../BaseComponent.js";

const styles = `
    :host {
      display: inline-block;
    }
    button {
      background-color: var(--blue-color);
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
      background-color: white;
      color: var(--grey-color);
      cursor: not-allowed;
    }
`;

class AppButtonPaginationNext extends BaseComponent {
  constructor() {
    super();
  }

  connectedCallback() {
    // this.applyStyles(styles);
    this.shadowRoot.innerHTML = `
        <style>${styles}</style>
        <button>
          <slot></slot>
        </button>
    `;

    this.setupSubmitBehavior(this.shadowRoot.querySelector("button"));
  }
}

customElements.define("app-button-pagination-next", AppButtonPaginationNext);
