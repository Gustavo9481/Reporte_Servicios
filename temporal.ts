// temporal.ts - Versión TypeScript de AppButtonBlue, sin características adicionales.

// Asumimos que BaseComponent también se adaptará a TypeScript o se importará como módulo JS.
// Si BaseComponent no es TypeScript, necesitarías una declaración de módulo o un archivo .d.ts para él.
import { BaseComponent } from "./BaseComponent.js"; // Ajusta la ruta si es necesario.

const styles: string = `
    :host {
        display: inline-block;
        min-width: 140px;
    }
    button {
        background-color: var(--blue-color);
        color: var(--white-color);
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
        background-color: var(--blue-darker);
    }
`;

/**
 * @class AppButtonBlue
 * @extends BaseComponent
 * @description Un componente web personalizado para botones azules rectangulares,
 *              duplicando la funcionalidad existente en JavaScript pero con tipado TypeScript.
 */
class AppButtonBlue extends BaseComponent {
    constructor() {
        super();
        // El Shadow DOM se adjunta en BaseComponent, como se infiere de applyStyles y shadowRoot.
    }

    /**
     * @method connectedCallback
     * @description Se invoca cada vez que el componente es añadido al DOM del documento.
     */
    connectedCallback(): void {
        this.applyStyles(styles); // Asume que applyStyles es un método de BaseComponent que usa el Shadow DOM.
        if (this.shadowRoot) { // Comprobación de nulidad para shadowRoot, ya que TypeScript puede no saber que siempre existe.
          this.shadowRoot.innerHTML += `
              <button>
                  <slot></slot>
              </button>
          `;
        }


        // Asumimos que setupSubmitBehavior es un método de BaseComponent o una función global accesible.
        // Si no está definido en BaseComponent, TypeScript requerirá su definición.
        if (this.shadowRoot?.querySelector("button")) {
            this.setupSubmitBehavior(this.shadowRoot.querySelector("button"));
        }
    }
}

customElements.define("app-button-blue", AppButtonBlue);
