# Blog Django - Projeto ES

Este é um projeto de blog desenvolvido com Python e Django. O blog tem como principal funcionalidade a exibição de postagens.

## Informações do Projeto

- **Universidade**: UNIVESIDADE FEDERAL DO TOCANTINS
- **Curso**: CIENCIAS DA COMPUTACAO
- **Disciplina**: ENGENHARIA DE SOFTWARE
- **Semestre**: 2025/01
- **Professor**: Edeilson Milhomem da Silva
- **Equipe**: Jonata Rubens Silva Araujo, Afonso Dglan Cirqueira Rodrigues, Carlos Eduardo Ribeiro Lima, Marcus Vinicius Guimaraes Balbino

## Tecnologias Utilizadas

- Python 3.x
- Django (versão mais recente)
- HTML, CSS e Bootstrap (para estilização)

## Funcionalidades

- Criar, editar e deletar postagens
- Exibir postagens publicadas
- Interface responsiva

## Instalação

### Pré-requisitos

Certifique-se de ter o Python e o Git instalados no sistema.

1. Clone este repositório:

   ```bash
   git clone https://github.com/JonataRubens/ES.git
   cd ES
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

Acesse o blog em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Estrutura do Projeto

```
ES/
│── blog/               # Aplicação principal do blog
│── static/             # Arquivos estáticos (CSS, JS, imagens)
│── templates/          # Templates HTML do Django
│── manage.py           # Comando de gerenciamento do Django
│── requirements.txt    # Dependências do projeto
│── README.md           # Este arquivo
```

## Contribuição

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

## Licença

Este projeto está sob a licença MIT.

