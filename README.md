# Blog Django - Projeto ES

Este é um projeto de blog desenvolvido com Python e Django, parte do repositório **ES**. O blog permite a criação e exibição de posts.

## Tecnologias Utilizadas

- Python 3.13.2
- Django (versão mais atual)
- HTML, CSS e Bootstrap (para estilização)

## Funcionalidades

- CRUD de postagens
- Interface responsiva

## Instalação

### Pré-requisitos

Certifique-se de ter o Python e o Git instalados em seu sistema.

1. Clone este repositório:

   bash
   git clone https://github.com/JonataRubens/ES.git
   cd ES
   

2. Crie um ambiente virtual e ative-o:

   bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   

3. Instale as dependências:

   bash
   pip install -r requirements.txt
   

4. Inicie o servidor de desenvolvimento:

   bash
   python manage.py runserver
   

Acesse o blog em http://127.0.0.1:8000/.

## Estrutura do Projeto


ES
blog                 - Aplicação principal do blog
stati              - Arquivos estáticos (CSS, JS, imagens)
templates            - Templates HTML do Django
manage.py             - Comando de gerenciamento do Django
requirements.txt      - Dependências do projeto
README.md             - Este arquivo


# Contribuição

1. Faça um fork do repositório
2. Crie uma branch para sua feature (git checkout -b minha-feature)
3. Commit suas alterações (git commit -m Minha nova feature)
4. Envie para o repositório remoto (git push origin minha-feature)
5. Abra um Pull Request


