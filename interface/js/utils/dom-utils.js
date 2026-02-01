// MÓDULO: interface/js/utils/dom-utils.js

/**
 * Muestra contenido HTML en un elemento del DOM.
 * @param {HTMLElement} element - El elemento del DOM donde se mostrará el contenido.
 * @param {string} htmlContent - El contenido HTML a mostrar.
 */
export const showContent = (element, htmlContent) => {
    if (element) {
        element.innerHTML = htmlContent;
    } else {
        console.error("El elemento para mostrar contenido no fue encontrado.");
    }
};