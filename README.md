# CxxTag
C++ is performant and powerful language. Bringing it's capabilities to the web platform will make it a greate place to code for.
For now we can only have C++ compiled in the build step of the app. It is not as flexible and does not really fit dinamic nature
of web applications.
The aim of the project is to achieve ease of use of C++ with web platform.

## What I want to achive
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
