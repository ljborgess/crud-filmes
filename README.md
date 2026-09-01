# Catálogo de Filmes

CRUD simples de filmes construído com Django, usando formulários HTML puros (sem Django Forms e sem Django REST Framework) e banco de dados SQLite.

## Stack

- Django 5.2
- SQLite (padrão do Django)
- HTML/CSS puro (sem frameworks front-end)

## Instalação e execução

```bash
# 1. Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# 2. Instalar as dependências
pip install -r requirements.txt

# 3. Aplicar as migrations (já inclui 5 filmes de exemplo)
python manage.py migrate

# 4. (Opcional) Criar um superusuário para acessar o admin
python manage.py createsuperuser

# 5. Rodar o servidor de desenvolvimento
python manage.py runserver
```

A aplicação estará disponível em `http://127.0.0.1:8000/filme/`.

## Endpoints

| Método | URL                       | Descrição                              |
|--------|---------------------------|-----------------------------------------|
| GET    | `/filme/`                 | Lista todos os filmes cadastrados       |
| GET/POST | `/filme/novo/`           | Formulário de criação de um novo filme  |
| GET/POST | `/filme/<pk>/editar/`    | Formulário de edição de um filme        |
| GET/POST | `/filme/<pk>/excluir/`   | Confirmação e exclusão de um filme      |
| GET    | `/admin/`                 | Painel administrativo do Django         |

## Modelo de dados

### Genero

| Campo   | Tipo      | Restrições              |
|---------|-----------|--------------------------|
| nome    | CharField | max_length=100, unique  |

### Filme

| Campo     | Tipo         | Restrições                                    |
|-----------|--------------|-------------------------------------------------|
| titulo    | CharField    | max_length=100                                  |
| genero    | ForeignKey   | para `Genero`, on_delete=PROTECT               |
| sinopse   | TextField    | max_length=280                                  |

Cada filme pertence a um gênero cadastrado à parte (relação N:1) — o formulário de cadastro exibe um `<select>` com os gêneros existentes em vez de um campo de texto livre. `on_delete=PROTECT` impede que um gênero seja excluído enquanto houver filmes vinculados a ele.

## CRUD direto pela listagem

A tela inicial (`/filme/`) exibe todos os filmes cadastrados em formato de cards e concentra todo o fluxo de CRUD:

- **Criar**: botão "Novo Filme" no topo da página leva ao formulário de cadastro.
- **Ler**: os filmes cadastrados aparecem automaticamente como cards na listagem, com título, gênero e sinopse.
- **Atualizar**: cada card tem um botão "Editar" que abre o mesmo formulário de cadastro, pré-preenchido com os dados do filme.
- **Excluir**: cada card tem um botão "Excluir" que leva a uma tela de confirmação antes de remover o filme definitivamente.

Não há paginação, busca ou filtros — o objetivo é um CRUD simples e direto para fins didáticos/apresentação.
