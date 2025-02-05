from setuptools import setup, find_packages

setup(
    name="ChangeTrackDB",           # Nome do seu pacote
    version="0.1.0",                   # Versão do pacote
    packages=find_packages(),          # Localiza pacotes automaticamente
    install_requires=[                 # Dependências necessárias
        "pymongo",                      # Dependência do pymongo
    ],
    entry_points={                     # (Opcional) Define comandos CLI
        'console_scripts': [
            'mongo-monitor=my_mongo_monitor.monitor:startMonitoring',  # Comando para iniciar a monitorização
        ],
    },
    author="Faceless",                 # Seu nome
    author_email="facelxss@proton.me", # Seu email
    description="Monitoramento em tempo real de mudanças no MongoDB", # Descrição do seu pacote
    long_description=open('README.md').read(),  # Lê a descrição longa do arquivo README.md
    long_description_content_type="text/markdown",  # Formato do arquivo README
    url="https://github.com/Facelless",  # URL do seu repositório
    classifiers=[                     # Classificadores que ajudam a categorizar seu pacote
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',           # Versão mínima do Python
)
