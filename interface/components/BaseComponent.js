// MÓDULO: interface/components/BaseComponent.js
// Calse madre para web components.

export class BaseComponent extends HTMLElement {

    constructor() {
        super();
        this.attachShadow({ mode: "open" });
    }

    /**
     * Aplica los estilos CSS al Shadow DOM del componente.
     * @param {string} styles - Cadena de texto con el contenido CSS.
     */
    applyStyles(styles) {
        const styleElement = document.createElement("style");
        styleElement.textContent = styles;
        this.shadowRoot.appendChild(styleElement);
    }

    /**
     * Configura el comportamiento del botón interno, incluyendo soporte para
     * 'submit'.
     * @param {HTMLButtonElement} buttonElement - El elemento botón dentro del
     * Shadow DOM.
     */
    setupSubmitBehavior(buttonElement) {
        // Establecer 'button' por defecto para evitar submits accidentales en formularios.
        buttonElement.type = "button";

        // Si el componente tiene un atributo 'type', aplicarlo al botón interno.
        if (this.hasAttribute("type")) {
            buttonElement.type = this.getAttribute("type");
        }

        buttonElement.addEventListener("click", (event) => {
            // Manejo especial para type="submit" dentro de Shadow DOM
            if (buttonElement.type === "submit") {
                const form = this.closest("form");
                if (form) {
                    // Crear un botón de submit temporal fuera del Shadow DOM
                    const tempSubmit = document.createElement("button");
                    tempSubmit.type = "submit";
                    tempSubmit.style.display = "none";
                    form.appendChild(tempSubmit);
                    tempSubmit.click();
                    form.removeChild(tempSubmit);
                    return; // Detener propagación adicional
                }
            }

            // Para clicks normales, despachar evento al componente principal.
            this.dispatchEvent(
                new MouseEvent("click", {
                    bubbles: true,
                    composed: true,
                })
            );
        });
    }
}
