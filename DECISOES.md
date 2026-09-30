# Decisões de projeto

Registro das decisões tomadas antes da implementação da 2ª etapa do trabalho.

**Contexto:** dar continuidade ao CRUD apresentado no bimestre passado, passando de 1 model para 4 tabelas no banco, com pelo menos uma cardinalidade 1:N.

---

## 1. Escopo: CRUD completo nos 4 models

Cada um dos 4 models tem suas quatro telas — criar, listar, editar e excluir.

**Por quê:** o enunciado pede "CRUD com 4 models". Ter 4 tabelas mas telas para apenas uma pode ser lido como requisito não cumprido. Como a nota do trabalho pode substituir a da prova, o custo de interpretar para menos é alto.

**Descartado:** CRUD apenas em Filme, com os outros 3 vivendo só no admin.

## 2. Schema: Genero, Filme, Diretor, Avaliação

O bimestre passado já tinha **dois** models (`Genero` e `Filme`), não um. Faltavam dois, não três.

**Por quê:** `Diretor` e `Avaliação` cabem no domínio sem inventar entidade artificial, e dão 1:N em sentidos opostos.

**Descartado:** `Ator` com ManyToMany — o Django cria uma 5ª tabela de junção por baixo, o que bagunçaria a contagem de "4 tabelas". `Estúdio` — ficaria quase idêntico a `Diretor`, com duas telas repetitivas.

## 3. Cardinalidades

| Relação | Tipo |
|---|---|
| Genero → Filme | 1:N (já existia) |
| Diretor → Filme | 1:N (nova) |
| Filme → Avaliação | 1:N (nova) |

**Por quê:** três relações 1:N em vez do mínimo de uma. `Diretor → Filme` coloca o model novo do lado "1"; `Filme → Avaliação` coloca o Filme do lado "1". Os dois sentidos ficam demonstrados.

## 4. on_delete: PROTECT no Diretor, CASCADE na Avaliação

- Excluir um **Diretor** com filmes é **bloqueado** (`PROTECT`), igual ao `Genero` que já era assim.
- Excluir um **Filme** apaga junto as **avaliações** dele (`CASCADE`).

**Por quê:** a diferença é proposital. Um diretor existe independentemente dos filmes, então não pode sumir e deixar registros órfãos. Uma avaliação só existe em função do filme — sem o filme, ela não significa nada. É a resposta pronta caso o professor pergunte por que o comportamento difere.

**Descartado:** CASCADE nos dois — um clique errado na demo apagaria meio banco. PROTECT nos dois — obrigaria apagar avaliação por avaliação antes de excluir um filme.

## 5. Model Diretor: nome + nacionalidade

**Por quê:** dois campos dão conteúdo ao card sem inventar complexidade, e `nacionalidade` rende um badge visual como o do gênero.

**Descartado:** incluir data de nascimento — mais um campo para preencher em toda demonstração.

## 6. Model Avaliação: nota 1–5, comentário, autor, criado_em

`nota` é `IntegerField` com validators de 1 a 5, renderizada como estrelas. `autor` é texto livre, sem login nem `User` do Django.

**Por quê:** escala de 1 a 5 é a mais visual e permite exibir média por filme. Autor como texto livre mantém o projeto simples e permite avatar com a inicial, como já fazem os cards de filme.

## 7. App renomeado de `filme` para `catalogo`

**Por quê:** o app passa a conter quatro models, então `filme` ficou mais estreito que o conteúdo.

**Por que é seguro:** renomear app Django normalmente dá problema com migrations, mas aqui `db.sqlite3` está no `.gitignore` e o seed recria os dados. As migrations podem ser apagadas e geradas de novo.

## 8. Views como função

As 16 views (4 models × 4 operações) continuam sendo funções.

**Por quê:** mantém o estilo já apresentado no bimestre passado e permite explicar cada view na arguição. Class-based views reduziriam para ~40 linhas, mas a lógica ficaria implícita no framework — arriscado se a turma não viu CBV em aula.

## 9. Django Forms (ModelForm)

Substitui o `request.POST['campo']` direto usado antes.

**Por quê:** o código atual quebra com `MultiValueDictKeyError` se um campo faltar, e não valida nada. Com 4 models isso seria 4× a chance de erro na apresentação. `ModelForm` valida, repopula o formulário com erro e corta boilerplate.

**Nota:** não usar Django Forms foi escolha do grupo no bimestre passado, não exigência do professor.

## 10. Templates: base.html + CSS em arquivo estático

Um `base.html` com layout e navegação; o CSS em `catalogo/static/catalogo/style.css`.

**Por quê:** o CSS estava duplicado inline nos 3 templates (~6 KB cada). Com 4 models seriam ~13 templates, ou seja, 13 cópias do mesmo CSS para manter em sincronia. `django.contrib.staticfiles` e `STATIC_URL` já estavam configurados.

## 11. Design pela skill `impeccable`

Direção criativa e futurista, aplicada depois que as telas existirem.

**Por quê:** desenhar antes dos models existirem seria desenhar tela vazia. O `base.html` + CSS único é a base sobre a qual o design atua de forma coerente nas 13 telas.

## 12. Dashboard na raiz

A rota `/` passa a ser uma dashboard com:

- contagem das 4 tabelas
- últimos filmes cadastrados
- últimas avaliações
- filme mais bem avaliado (média de estrelas)

**Por quê:** hoje `/` devolve **404** — só existem `admin/` e `filme/`. Além de corrigir isso, a dashboard comunica os 4 models de imediato e mostra as relações 1:N funcionando sem precisar navegar.

**Descartado:** gráficos. O pedido foi explicitamente "simples".

## 13. Seed com diretores e avaliações

O seed passa a criar diretores para os 5 filmes existentes e 2–3 avaliações por filme.

**Por quê:** `Diretor` é obrigatório, então os filmes existentes precisam de um. E a demonstração é ao vivo — nenhuma tela pode abrir vazia, ou a média de estrelas não aparece.

## 14. Artefato de apresentação: slides

Construído **depois** do código, não durante.

**Por quê:** é o formato esperado numa apresentação de sala e projeta bem. Cobre contexto, diagrama dos models, relações, decisões e demonstração.

## 15. Material a coletar durante a implementação

- diagrama do banco com as 4 tabelas e as setas 1:N
- comparativo antes/depois (1 CRUD com 2 models → 4 CRUDs com 4 models)

**Fora de escopo:** capturas de tela. A demonstração será ao vivo, e é por isso que o seed populado da decisão 13 importa.

---

## Ajustes menores decididos por padrão

- URLs no plural: `/filmes/`, `/diretores/`, `/generos/`, `/avaliacoes/`
- `TIME_ZONE` de `UTC` para `America/Sao_Paulo` — necessário para o `criado_em` das avaliações não aparecer 3 horas adiantado
- `Genero` ganha telas próprias de CRUD, que não tinha
- `admin.py` registra os 4 models
- README reescrito com o novo modelo de dados

---

## Pendência

O **enunciado oficial no Teams ainda não foi conferido**. Estas decisões partiram do recado repassado pelo grupo. Requisitos como autenticação, upload de imagem ou deploy mudariam parte do plano.
