from setuptools import setup, find_packages

setup(
    name="DLLBridge",  # Nome do pacote
    version="0.1.0",  # Versão do pacote
    description="A simple Python library to interact with DLLs on Windows.",  # Descrição curta
    long_description=open('README.md').read(),  # Descrição longa extraída do README.md
    long_description_content_type='text/markdown',  # Tipo do conteúdo do README.md
    author="Leonardo",  # Seu nome ou nome da organização
    author_email="leonardonery616@gmail.com",  # Seu e-mail de contato
    packages=find_packages(),  # Encontra automaticamente todos os pacotes do seu projeto
    install_requires=[],  # Nenhuma dependência externa é necessária, pois 'os' e 'ctypes' são nativos
    classifiers=[
        "Programming Language :: Python :: 3",  # Especifica que o projeto é para Python 3
        "License :: OSI Approved :: MIT License",  # Licença do projeto
        "Operating System :: Microsoft :: Windows",  # Especifica que é para sistemas Windows
        "Intended Audience :: Developers",  # Público alvo
    ],
    python_requires=">=3.6",  # Versão mínima do Python necessária
)
