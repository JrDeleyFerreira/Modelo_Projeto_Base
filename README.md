# Modelo Base de criação com pacote UV

## Instalação e passo a passo na criação de um projeto Python com pacote uv:

01. Instalação:
    - pip install uv
02. Criação do projeto:
    - uv init (dentro da pasta gerando os arquivos)
    - uv init 'nome do projeto'
03. Criar ambiente virtual:
    - py -m venv .venv
    - No arquivo .python-version, vai especificar a versão da VM
    - Arquivo pyproject.toml -> Informações diversas sobre novo projeto

### Projeto Django

01. Instalação:
    - django-admin startproject 'nome do projeto' .
02. Gerar arquivo de listagem de pacotes utilizados:
    - pip freeze > requirements.txt