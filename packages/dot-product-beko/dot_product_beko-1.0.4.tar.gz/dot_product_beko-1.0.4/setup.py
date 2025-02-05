from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import platform
import subprocess
import os

lib_name = "dot_product.so" if platform.system() != "Windows" else "dot_product.dll"
# Proje kök dizinine göre mutlak yol hesaplayalım:
here = os.path.abspath(os.path.dirname(__file__))
lib_path = os.path.join(here, "dot_product", lib_name)

# Özel derleme komutu: Bu komut, nasm ve gcc'yi çağırıp shared library'yi oluşturur.
class BuildLibrary(build_ext):
    def run(self):
        try:
            if platform.system() == "Windows":
                subprocess.run(
                    ["nasm", "-f", "win64", "src/dot_product.asm", "-o", "src/dot_product.o"],
                    check=True
                )
                subprocess.run(
                    ["gcc", "-shared", "-o", lib_path, "src/dot_product.c", "src/dot_product.o", "-nostartfiles"],
                    check=True
                )
            else:
                subprocess.run(
                    ["nasm", "-f", "elf64", "src/dot_product.asm", "-o", "src/dot_product.o"],
                    check=True
                )
                subprocess.run(
                    ["gcc", "-shared", "-o", lib_path, "src/dot_product.c", "src/dot_product.o", "-nostartfiles", "-fPIC"],
                    check=True
                )
        except Exception as e:
            # Derleme hatası durumunda burada hata fırlatıp pip install işlemini iptal edelim.
            raise RuntimeError(f"Shared library derlemesi başarısız: {e}")
        # Eğer derleme başarılıysa, normal build_ext işlemini devam ettiriyoruz.
        super().run()

# Dummy uzantı tanımı: build_ext komutunun çalışmasını tetiklemek için kullanılacak.
# Bu dosya, örneğin src/dummy.c dosyasında çok basit bir C kodu içerebilir.
# src/dummy.c içeriği örneğin:
#    /* dummy file */
#    void dummy() {}
dummy_extension = Extension("dummy", sources=["src/dummy.c"])

setup(
    name="dot_product_beko",
    version="1.0.4",
    description="Fast dot product computation using Assembly (AVX2)",
    author="Abdulhamit Güngören",
    author_email="abdulhamitgungoren@gmail.com",
    packages=["dot_product"],
    # Derlenmiş shared library'yi paket içine dahil et:
    package_data={"dot_product": [lib_name]},
    install_requires=["numpy"],
    cmdclass={"build_ext": BuildLibrary},
    # Dummy extension sayesinde build_ext komutu her zaman çağrılacak.
    ext_modules=[dummy_extension]
)
