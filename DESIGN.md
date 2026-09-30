# Design — Cátodo Velado

Sistema visual do Catálogo de Filmes, registrado a partir do que foi construído.

**Origem:** mundo `operate-b-struck-cathode-gauze`, escolhido pelo usuário sobre a direção sorteada. Topologia de fileiras doada do padrão de streaming, a pedido dele. Seed `cf89399c`.

## Princípio

Todo valor possível está na tela ao mesmo tempo, como fantasma apagado atrás de uma tela de bronze. O valor em vigor é **golpeado à frente**, aceso. Nada é revelado por transição suave: o novo golpeia, o antigo decai.

## Cores

Duas cores, quatro papéis. Não há terceira cor.

| Token | Valor | Papel |
|---|---|---|
| `--fundo` | `#070a12` | chão azul-tinta |
| `--fundo-fundo` | `#04060c` | trilho de rolagem |
| `--malha` | `rgba(200,160,106,.3)` | tecido de bronze |
| `--fantasma` | `rgba(226,214,196,.42)` | valor apagado |
| `--fantasma-fraco` | `rgba(226,214,196,.3)` | contorno das irmãs |
| `--golpe` | `#ff7a1c` | cátodo aceso |
| `--golpe-claro` | `#ffa257` | atributo |
| `--osso` | `#efe7da` | prosa |
| `--osso-fraco` | `rgba(239,231,218,.62)` | prosa secundária |
| `--recusa` | `rgba(239,231,218,.22)` | recusado, desligado |

`#ff5a3c` aparece só em erro de formulário e exclusão — não é cor do sistema, é sinal.

## Tipografia

- **Display:** Saira Condensed 900, caixa alta, `letter-spacing: -0.02em`. Numerais e títulos.
- **Prosa:** Barlow 400/500/600.
- **Rótulo:** Barlow Condensed 600, caixa alta, `letter-spacing: .22em`.

Títulos monumentais e numerais são **recortados da malha** (`background-clip: text` sobre duas `repeating-linear-gradient` escuras mais a cor base). A letra é feita do tecido, não pintada por cima dele. O detector mecânico sinaliza isso como "gradient text": é falso positivo, a malha é a assinatura do mundo.

Recorte na malha corta diacríticos, então todo elemento malhado usa `line-height ≥ 1.02` e `padding-top: .06em`. Sem isso o til do "Ã" some.

## Composição

**Sem caixa, régua ou divisória.** Não existe `border` de contorno, `card`, nem separador horizontal em lugar nenhum. O agrupamento vem de densidade de malha, profundidade e espaço.

A malha (`.gauze`) é `position: fixed`, corre 10vh/10vw além de toda borda, e tem máscara radial para não ter fim visível.

Listagens usam grade de `auto-fill` com mínimo de 290px. Faixas horizontais usam `overflow-x: auto` com `mask-image` que desvanece o último item em vez de cortá-lo.

## Estados

| Estado | Rendição |
|---|---|
| em vigor | golpeado em `--golpe` com halo |
| disponível | `--osso` ou `--osso-fraco` |
| apagado | contorno em `--fantasma`, sem preenchimento |
| recusado | `--recusa`, escuro, sem halo |
| condenado | só contorno, em vermelho translúcido |

O bloqueio do `PROTECT` usa `.recusado`: fica escuro e explica o motivo. Não é tratado como erro vermelho, porque não é falha do usuário.

## Movimento

Um relógio só: `--beat: 220ms`, `--saida: cubic-bezier(.16,1,.3,1)`.

- `golpear` — entrada dos numerais, escalonada em 110ms por métrica, de desfoque para nítido
- `deriva` — a malha se desloca 4px em 32s, contínua
- hover — o título golpeia em laranja; o sublinhado da ação abre de `scaleX(0)`

Nada interpola valor. `prefers-reduced-motion` zera tudo.

## Superfícies do navegador

Seleção, cursor de texto, barras de rolagem e anel de foco são todos temáticos em `--golpe`. Numerais usam `tabular-nums`. Links herdam cor (`a { color: inherit }`) — sem isso o azul padrão vaza onde a cor vem de `background-clip`.

## Limitação conhecida

O layout abaixo de ~480px **não foi verificado por captura**: o Chromium headless impõe largura mínima de janela e renderiza ~480px mesmo quando 390px é pedido, recortando a imagem. As regras de `@media (max-width: 720px)` estão ativas e verificadas em 480px; larguras menores dependem dos limites amarrados à viewport (`min(68ch, calc(100vw - 2.6rem))`).
