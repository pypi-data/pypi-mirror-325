from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import platform
import subprocess
import os

# Dinamik kütüphane adını belirle (Windows: .dll, Linux: .so)
lib_name = "dot_product.so" if platform.system() != "Windows" else "dot_product.dll"
lib_path = os.path.join("dot_product", lib_name)

# Özel derleme komutu
class BuildLibrary(build_ext):
    def run(self):
        if platform.system() == "Windows":
            subprocess.run(["nasm", "-f", "win64", "src/dot_product.asm", "-o", "src/dot_product.o"], check=True)
            subprocess.run(["gcc", "-shared", "-o", lib_path, "src/dot_product.c", "src/dot_product.o", "-nostartfiles"], check=True)
        else:
            subprocess.run(["nasm", "-f", "elf64", "src/dot_product.asm", "-o", "src/dot_product.o"], check=True)
            subprocess.run(["gcc", "-shared", "-o", lib_path, "src/dot_product.c", "src/dot_product.o", "-nostartfiles", "-fPIC"], check=True)

        super().run()

# Setup fonksiyonu
setup(
    name="dot_product_beko",
    version="1.0.1",
    description="Fast dot product computation using Assembly (AVX2)",
    author="Abdulhamit Güngören",
    author_email="abdulhamitgungoren@gmail.com",
    packages=["dot_product"],
    package_data={"dot_product": [lib_name]},
    install_requires=["numpy"],
    cmdclass={"build_ext": BuildLibrary},
)
