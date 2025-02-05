import os
import platform
import ctypes

base_path = os.path.dirname(__file__)
if platform.system() == "Windows":
    lib_file = "libdot_product.dll"
else:
    lib_file = "libdot_product.so"

lib_path = os.path.join(base_path, lib_file)
lib = ctypes.CDLL(lib_path)

# Artık lib üzerinde, asm kodunuzun sunduğu fonksiyonları çağırabilirsiniz.
# Örneğin, eğer fonksiyon adınız "dot_product" ise:
# lib.dot_product.argtypes = [ctypes.POINTER(ctypes.c_double), ...]
# lib.dot_product.restype = ctypes.c_double

# Sonrasında, paket içindeki fonksiyonları tanımlayabilirsiniz:
def dot_product(x, y):
    # x, y numpy dizileri olsun, örneğin:
    # İlgili pointerleri elde edip lib.dot_product fonksiyonunu çağırın.
    pass

__all__ = ["dot_product"]
