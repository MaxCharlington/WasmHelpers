#include <string>
#include <cstdio>

double func(double a) {
    printf("%f\n", a);
    return a + 12;
}

std::string func2() {
    return "";
}

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
