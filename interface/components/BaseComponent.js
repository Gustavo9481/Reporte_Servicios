// MÓDULO: interface/components/BaseComponent.js

export class BaseComponent extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
    }

    /**
     * Aplica los estilos CSS al Shadow DOM del componente.
     * @param {string} styles - Una cadena de texto con el contenido CSS.
     */
    applyStyles(styles) {
        const styleElement = document.createElement("style");
        styleElement.textContent = styles;
        this.shadowRoot.appendChild(styleElement);
    }
}
