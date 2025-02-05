#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

extern double dot_product(double* x, double* y, uint64_t N);

double dot_product_c(double* x, double* y, uint64_t N) {
    return dot_product(x, y, N);
}

#ifdef __cplusplus
}
#endif
