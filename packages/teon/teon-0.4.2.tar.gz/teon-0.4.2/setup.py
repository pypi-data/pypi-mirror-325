from setuptools import setup, find_packages

setup(
    name="teon",
    version="0.4.2",
    packages=find_packages(),
    include_package_data=True,
    package_data={'teon': ['icon.png', 'Teon Level Editor.exe', 'extra/*'],},
    install_requires=[
        "pygame>=2.0.0",
        "opencv-python",
        "Pillow",
    ],
)
