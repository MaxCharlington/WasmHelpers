# Wasm helpers

JavaScript is the only true language that can be run by the browser. WebAssembly is not real competitor 
in this field as it's hard to write it manually. There are a lot of compiled, performant and powerful 
language that are capable to be executed in the web-browser through WebAssembly.
Bringing their capabilities to the web platform will make it a greate place to code for.
For now we can only have them compiled in the build step of the app. It is not as flexible and does not
really fit dynamic nature of web applications.
The aim of the project is to achieve ease of use of those languages with web platform by creating tools
for their integration.


## Option 1. Script tag

Direct script in non-native language is one of planned options.
Dream implementation will look like this:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
    <script language="cxx">
        union float_cast{
            float f;
            struct {
                unsigned int mantisa : 23;
                unsigned int exponent : 8;
                unsigned int sign : 1;
            } parts;
        };

        unsigned getMantissa(float num) {
            float_cast d1 = { .f = num };
            return d1.parts.mantisa;
        }
    </script>
    <script>
        console.log(getMantissa(0.2))  // Logs 5033165
    </script>
</body>
</html>
```
