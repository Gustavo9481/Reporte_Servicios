// MODULO: interface/components/app-button-pagination-next/app-button-pagination-next.js

// Componente personalizado para otón circular de paginación (< >).


import { BaseComponent } from "../BaseComponent.js";

const styles = `
    :host {
      display: inline-block;
    }
    button {
      background-color: var(--blue-color);
      color: white;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      transition: background-color 0.3s ease;
      width: 40px;
      height: 40px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2em;
      line-height: 1;
    }
    button:hover {
      background-color: var(--blue-darker);
    }
    button:disabled {
      background-color: var(white-color);
      color: var(--grey-color);
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

    this.setupSubmitBehavior(this.shadowRoot.querySelector("button"));
  }
}

customElements.define("app-button-pagination-next", AppButtonPaginationNext);
