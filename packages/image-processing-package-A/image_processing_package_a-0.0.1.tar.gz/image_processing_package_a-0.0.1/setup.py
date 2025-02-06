from setuptools import setup, find_packages

setup(
    name="image_processing_package-A",
    version="0.0.1",
    author="Amanda Diniz",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seuusuario/meu_pacote",
    packages=find_packages(),
    install_requires=[],  # Dependências do pacote
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)