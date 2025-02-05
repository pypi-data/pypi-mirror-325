import ctypes
import numpy as np
import platform
import os

# Dinamik kütüphaneyi yükleme
base_path = os.path.dirname(__file__)
if platform.system() == "Windows":
    lib_path = os.path.join(base_path, "libdot_product.dll")
else:
    lib_path = os.path.join(base_path, "libdot_product.so")

lib = ctypes.CDLL(lib_path)

# Fonksiyon prototipini ayarla
lib.dot_product_c.argtypes = [ctypes.POINTER(ctypes.c_double),
                               ctypes.POINTER(ctypes.c_double),
                               ctypes.c_uint64]
lib.dot_product_c.restype = ctypes.c_double

def dot_product(x: np.ndarray, y: np.ndarray) -> float:
    """ Assembly hızlandırılmış dot product hesaplama """
    assert x.shape == y.shape, "Vectors must have the same shape"
    assert x.dtype == np.float64, "Input must be float64"
    assert y.dtype == np.float64, "Input must be float64"

    N = x.shape[0]
    x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    y_ptr = y.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    return lib.dot_product_c(x_ptr, y_ptr, N)
