# Wasm helpers

[Documentation in English](README_en.md)

JavaScript - единственный язык, который можно запустить в браузере. WebAssembly не может ничего противопоставить,
так как его крайне сложно писать вручную. Есть множество компилируемых, производительных и мощных
язык, которые могут выполняться в веб-браузере через WebAssembly.
Если использовать их в браузере, это во многом улучшит платформу и расширит ее возможности.
На данный момент мы можем скомпилировать их только на этапе сборки приложения. Это не так гибко и не
соответствует динамчности веб-приложений.
Цель проекта - добиться простоты использования этих языков с веб-платформой путем создания инструментов
для их интеграции.


## Вариант 1. Использование тэга script

Использование ненативного языка непосредственно в тэге script.
Желаемый код, использующий этот подход:

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
