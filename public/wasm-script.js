class WasmScript extends HTMLElement {
    constructor() {
        super();
        this.style.display = 'none'
    }
    connectedCallback() {
        const sourceCode = this.innerText
        const initWasmScript = fetch('https://api.github.com/gists', {
            method: 'post',
            body: JSON.stringify(opts)
        }
    }
}

window.customElements.define('wasm-script', WasmScript);
