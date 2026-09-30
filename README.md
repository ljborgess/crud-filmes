# Catálogo de Filmes

CRUD em Django com **4 models** e **três relações 1:N**, usando `ModelForm`, templates com herança e banco SQLite.

Continuação do trabalho do bimestre anterior, que tinha 2 models (`Genero` e `Filme`) e telas de CRUD apenas para `Filme`.

## Stack

- Django 5.2
- SQLite (padrão do Django)
- HTML/CSS puro, sem frameworks front-end

## Instalação e execução

```bash
# 1. Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# 2. Instalar as dependências
pip install -r requirements.txt

# 3. Aplicar as migrations (o seed já popula todas as tabelas)
python manage.py migrate

# 4. (Opcional) Criar um superusuário para acessar o admin
python manage.py createsuperuser

# 5. Rodar o servidor
python manage.py runserver
```

A aplicação abre em `http://127.0.0.1:8000/`.

## Modelo de dados

```
Genero ──1:N──┐
              ├──> Filme ──1:N──> Avaliacao
Diretor ─1:N──┘
```

### Genero

| Campo | Tipo | Restrições |
|---|---|---|
| nome | CharField | max_length=100, unique |

### Diretor

| Campo | Tipo | Restrições |
|---|---|---|
| nome | CharField | max_length=100 |
| nacionalidade | CharField | max_length=60 |

### Filme

| Campo | Tipo | Restrições |
|---|---|---|
| titulo | CharField | max_length=100 |
| genero | ForeignKey → Genero | on_delete=PROTECT |
| diretor | ForeignKey → Diretor | on_delete=PROTECT |
| sinopse | TextField | max_length=280 |

### Avaliacao

| Campo | Tipo | Restrições |
|---|---|---|
| filme | ForeignKey → Filme | on_delete=CASCADE |
| autor | CharField | max_length=80 |
| nota | PositiveSmallIntegerField | validators de 1 a 5 |
| comentario | TextField | max_length=280, opcional |
| criado_em | DateTimeField | auto_now_add |

### As três relações 1:N

| Relação | Leitura |
|---|---|
| `Genero` → `Filme` | um gênero tem muitos filmes |
| `Diretor` → `Filme` | um diretor tem muitos filmes |
| `Filme` → `Avaliacao` | um filme tem muitas avaliações |

### Por que `PROTECT` em dois casos e `CASCADE` no outro

`Genero` e `Diretor` existem **independentemente** dos filmes. Apagar um gênero que ainda tem filmes deixaria registros órfãos, então o banco bloqueia (`PROTECT`) e a interface explica o motivo em vez de dar erro.

`Avaliacao` só existe **em função** do filme — uma nota sem o filme avaliado não significa nada. Por isso, apagar um filme apaga junto as avaliações dele (`CASCADE`).

## Telas

| URL | Descrição |
|---|---|
| `/` | Painel com as contagens, últimos filmes, últimas avaliações e o filme melhor avaliado |
| `/filmes/` | CRUD de filmes (lista, novo, editar, excluir) |
| `/diretores/` | CRUD de diretores |
| `/generos/` | CRUD de gêneros |
| `/avaliacoes/` | CRUD de avaliações |
| `/admin/` | Painel administrativo do Django |

Cada seção segue o mesmo padrão de rotas: `/`, `/novo/`, `/<pk>/editar/` e `/<pk>/excluir/`.

## Organização do código

```
core/                      configurações e rotas do projeto
catalogo/
  models.py                os 4 models
  forms.py                 um ModelForm por model
  views.py                 painel + 16 views de CRUD (funções)
  urls.py                  as 17 rotas
  admin.py                 os 4 models registrados no admin
  migrations/
    0001_initial.py        criação das tabelas
    0002_seed_catalogo.py  dados de exemplo
  static/catalogo/
    style.css              CSS único da aplicação
  templates/catalogo/
    base.html              layout e navegação
    dashboard.html         painel
    *_lista.html           uma listagem por model
    form.html              formulário compartilhado pelos 4 models
    confirmar_exclusao.html  confirmação compartilhada
    _estrelas.html         trecho reaproveitado das estrelas
```

As telas de formulário e de confirmação são **compartilhadas** pelos 4 models: o template percorre os campos do `ModelForm`, então são 9 templates em vez de 16.

## Decisões de projeto

As escolhas de modelagem e arquitetura, com as alternativas descartadas, estão em [DECISOES.md](DECISOES.md).
