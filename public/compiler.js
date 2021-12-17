// wait cxx script

// send code
const cxxScripts = Array.from(document.querySelectorAll('script[language="cxx"]'))
if (cxxScripts.length == 1)
{
    const sourceCode = cxxScripts[0].innerText
    // fetch
}
else if (cxxScripts > 1) 
{
    // Handle many scripts
}

// send calls?


// Compile


// publish recieved code
var Module = {
    onRuntimeInitialized: function() {
        console.log(Module.func(123.123))
    }
};
