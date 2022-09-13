class WasmScript extends HTMLElement {
    constructor() {
        super();
        this.style.display = 'none'
    }
    async connectedCallback() {
        const sourceCode = this.innerText
        const res = await fetch('http://localhost:3000/compile', {
            method: 'PUT',
            body: sourceCode
        })
        let s = document.createElement("script")
        s.type = "text/javascript"
        s.src = await res.text()
        document.body.appendChild(s);
    }
}

var Module = {
    onRuntimeInitialized: function() {
        console.log(Module.getMantissa(0.2))
    }
}

window.customElements.define('wasm-script', WasmScript);
