from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import platform
import subprocess
import os
import shutil  # dosya kopyalamak için

# Proje kök dizinini belirleyin
here = os.path.abspath(os.path.dirname(__file__))

# Shared library ismini belirleyin (Windows için .dll, diğer platformlar için .so)
lib_name = "dot_product.so" if platform.system() != "Windows" else "dot_product.dll"
# Shared library dosyasının hedef konumu: Paket dizini içinde (build aşaması öncesinde)
lib_path = os.path.join(here, "dot_product", lib_name)

class BuildLibrary(build_ext):
    def run(self):
        try:
            if platform.system() == "Windows":
                subprocess.run(
                    ["nasm", "-f", "win64", "src/dot_product.asm", "-o", os.path.join(here, "src", "dot_product.o")],
                    check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                subprocess.run(
                    ["gcc", "-shared", "-o", lib_path, os.path.join(here, "src", "dot_product.c"), os.path.join(here, "src", "dot_product.o"), "-nostartfiles"],
                    check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
            else:
                subprocess.run(
                    ["nasm", "-f", "elf64", "src/dot_product.asm", "-o", os.path.join(here, "src", "dot_product.o")],
                    check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                subprocess.run(
                    ["gcc", "-shared", "-o", lib_path, os.path.join(here, "src", "dot_product.c"), os.path.join(here, "src", "dot_product.o"), "-nostartfiles", "-fPIC"],
                    check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
        except Exception as e:
            raise RuntimeError(f"Shared library derlemesi başarısız: {e}")
        
        # Şimdi, build_ext'in build_lib dizinine shared library dosyasını kopyalayalım.
        # self.build_lib, build_ext çalışırken oluşturulan build ağacının yoludur.
        dest_dir = os.path.join(self.build_lib, "dot_product")
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, lib_name)
        shutil.copy(lib_path, dest_path)
        self.announce(f"Kopyalandı: {lib_path} -> {dest_path}", level=3)
        
        # Dummy extension'ı derleyerek build_ext'in çalıştığından emin oluyoruz.
        super().run()

# Dummy extension tanımı; build_ext'in çalışmasını garanti altına almak için
# Basit bir dummy C dosyası oluşturun: src/dummy.c içeriği şöyle olabilir:
#    /* src/dummy.c */
#    void dummy() {}
dummy_extension = Extension("dummy", sources=[os.path.join("src", "dummy.c")])

setup(
    name="dot_product_beko",
    version="1.0.5",
    description="Fast dot product computation using Assembly (AVX2)",
    author="Abdulhamit Güngören",
    author_email="abdulhamitgungoren@gmail.com",
    packages=["dot_product"],
    # package_data, wheel oluşturulurken bu dosyanın dahil edilmesini sağlar
    package_data={"dot_product": [lib_name]},
    install_requires=["numpy"],
    cmdclass={"build_ext": BuildLibrary},
    ext_modules=[dummy_extension]
)
