# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Dois públicos, com objetivos diferentes:

- **O autor do trabalho**, que opera o sistema ao vivo durante a apresentação. Precisa navegar entre as telas com segurança, sem tela vazia e sem erro, enquanto fala.
- **O professor avaliador (Malerba)**, que assiste e julga. Precisa reconhecer em poucos segundos que existem 4 tabelas, que há relações 1 para muitos, e que o CRUD funciona nas quatro.

## Product Purpose

Catálogo de filmes com cadastro completo de gêneros, diretores, filmes e avaliações.

O propósito acadêmico é demonstrar 4 models com pelo menos uma cardinalidade 1:N, dando continuidade a um CRUD de 2 models apresentado no bimestre anterior. O trabalho pode substituir a nota da prova, na proporção 60/40, se a execução for considerada muito boa.

## Operating Context

- Apresentação em sala, com **demonstração ao vivo** — não há capturas de tela de apoio.
- O banco vem populado por uma migration de seed, para que nenhuma tela abra vazia durante a demonstração.
- O avaliador pode pedir para ver qualquer operação, inclusive exclusão, então os estados de bloqueio precisam se explicar sozinhos.
- Roda no servidor de desenvolvimento do Django, em `localhost`.

## Capabilities and Constraints

**Funcionalidade confirmada:**

- CRUD completo (criar, listar, editar, excluir) para os 4 models: `Genero`, `Diretor`, `Filme`, `Avaliacao`.
- Painel na raiz com contagem das 4 tabelas, últimos filmes, últimas avaliações e o filme com maior média de notas.
- Três relações 1:N: Genero→Filme, Diretor→Filme, Filme→Avaliacao.
- Regras de exclusão: `PROTECT` em Genero e Diretor (bloqueia e explica o motivo na interface), `CASCADE` em Avaliacao.
- Validação via `ModelForm`, incluindo nota restrita a 1–5 e nome de gênero único.
- Avaliação usa autor como texto livre. **Não há login, autenticação nem model de usuário.**

**Restrições técnicas:**

- Django 5.2 com SQLite.
- HTML e CSS puros. **Sem framework front-end e sem etapa de build.**
- Sem restrição imposta pelo professor quanto a bibliotecas externas, CDN ou fontes.
- Padrão de código deliberadamente simples: views como função, sem `.env` nem camada extra de segurança.

## Brand Commitments

- Nome atual na interface: **Catálogo de Filmes**.
- O sistema deve se apresentar **como um produto real**, sem mencionar trabalho, turma, bimestre ou disciplina nas telas. O enquadramento acadêmico fica nos slides de apresentação, não na interface.
- Pedido visual explícito e vinculante: direção **criativa e futurista**, com **movimento acentuado** (animação como parte da identidade, não enfeite).

## Evidence on Hand

- Seed com 5 filmes reais e seus diretores verdadeiros (`catalogo/migrations/0002_seed_catalogo.py`).
- 12 avaliações com autores e comentários **fictícios**, criados para popular a demonstração.
- Não existem usuários reais, métricas de uso, depoimentos ou parceiros. Nada disso pode ser inventado na interface.
- Decisões de arquitetura registradas em `DECISOES.md`.

## Product Principles

1. **A demonstração é o produto.** Qualquer tela pode ser aberta na frente do avaliador; nenhuma pode estar vazia, quebrada ou ambígua.
2. **As quatro tabelas precisam ser óbvias.** A estrutura de dados é o requisito avaliado, então a interface deve tornar as entidades e suas relações visíveis sem explicação verbal.
3. **Bloqueio se explica.** Quando o `PROTECT` impede uma exclusão, a tela diz o porquê e o que fazer — nunca devolve erro cru.
4. **Simplicidade no código, ambição no visual.** O back-end fica legível e defensável em arguição; o investimento de ousadia vai para a interface.

## Open decisions

- O enunciado oficial no Teams ainda não foi conferido. Requisitos como autenticação, upload de imagem ou deploy mudariam as capacidades acima.
- O formato do artefato de apresentação foi definido como slides, mas o usuário mencionou a possibilidade de usar um artefato publicado. Ainda não resolvido.
