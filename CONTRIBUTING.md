# Como colaborar com esta wiki

Bem-vindo. Este guia é para quem vai escrever ou corrigir um verbete. Ele é longo de
propósito: a ideia é que você consiga contribuir sem precisar perguntar nada a ninguém.

Se algo aqui estiver confuso, abra uma questão dizendo o que não entendeu. Guia que só
funciona para quem já sabe não serve.

## O que esta wiki é

É uma rede de verbetes curtos sobre uma disciplina de métodos de pesquisa. Cada verbete é um
arquivo de texto, e os verbetes se ligam uns aos outros formando um grafo, isto é, um mapa de
relações entre ideias, autores e leituras.

O que distingue esta wiki de um caderno de anotações é uma regra só: **toda afirmação sobre o
que uma leitura diz precisa vir com a passagem citada e a página**. Não vale escrever que o
autor sustenta alguma coisa e deixar o leitor confiar. A passagem entra no arquivo, e um
programa confere se ela existe mesmo naquela página.

## Antes de começar, entenda os seis tipos

Cada verbete é de um tipo, e o tipo decide em que pasta ele mora:

| Tipo | Pasta | O que é |
|---|---|---|
| `concept` | `conceitos/` | Uma ideia da disciplina, como desenho de pesquisa ou mecanismo |
| `text` | `textos/` | Um artigo ou capítulo da bibliografia |
| `author` | `autores/` | Quem escreveu os textos |
| `session` | `sessoes/` | Uma aula, com as leituras dela |
| `legislation` | `legislacao/` | Uma norma |
| `julgado` | `julgados/` | Uma decisão judicial |

O nome do arquivo é o identificador do verbete, sempre em letras minúsculas, sem acento e com
hífen no lugar do espaço. Por exemplo, o conceito "desenho de pesquisa" vira
`conceitos/desenho-de-pesquisa.md`.

## Anatomia de um verbete

Todo arquivo começa com um cabeçalho entre duas linhas de três traços. Esse cabeçalho é o que
o programa lê; o texto que vem depois é o que a pessoa lê.

```
---
schema_version: 1
type: concept
slug: desenho-de-pesquisa
title: "Desenho de pesquisa"
status: complete
note_type: conceitual
---

# Desenho de pesquisa

O texto do verbete vem aqui.
```

Os seis campos acima são obrigatórios em qualquer tipo. O campo `status` diz em que pé está o
verbete: use `stub` se ele ainda é um esboço e `complete` quando estiver pronto.

### O que muda em cada tipo

Um verbete de **texto** precisa dizer de onde vem a leitura e o que ela sustenta. É nele que
mora a exigência de citar:

```
---
schema_version: 1
type: text
slug: alvesson-sandberg-2011
title: "Generating Research Questions Through Problematization"
status: complete
note_type: literaria
authors: [alvesson, sandberg]
sessions:
  - id: s02-03
    role: obrigatoria
concepts:
  - id: problematizacao
    evidence:
      - page: 1
        excerpt: "We propose problematization as a methodology for identifying and challenging assumptions underlying existing literature."
sources:
  - path: "caminho/para/a/copia/em/texto/do/artigo.md"
tags: [S02-03, problematizacao]
verificacoes: []
---
```

Repare no bloco `evidence`: para cada conceito que o texto desenvolve, você declara a página e
a passagem exata. **A passagem é copiada, nunca digitada de memória nem resumida.** É essa
literalidade que o programa confere.

Um verbete de **decisão judicial** ou de **norma** exige ao menos duas marcas no campo
`verificacoes`, porque documento oficial circula em versões diferentes e precisa de mais de um
ponto de conferência.

## As duas maneiras de ligar verbetes

Escrever `[[nome-do-verbete]]` cria uma ligação. O efeito depende de onde você escreve:

**Dentro de um verbete de conceito**, a ligação cria uma aresta no grafo, quer dizer, uma
relação registrada nos dois sentidos. Se o verbete de "comensurabilidade" liga para "desenho
de pesquisa", os dois passam a se saber relacionados.

**Em qualquer outro lugar**, a ligação é só navegação: ajuda o leitor a chegar em outra
página e não muda o mapa de relações.

Você também pode escrever `[[nome-do-verbete|o texto que aparece]]` quando quiser que o link
apareça com outras palavras, o que é comum quando a frase pede o termo no plural ou com
acento.

**Relação que tem significado vai no cabeçalho, e nunca só no corpo do texto.** Se um artigo
desenvolve um conceito, isso entra no bloco `concepts` do cabeçalho, com a passagem citada. A
ligação no meio do parágrafo é um atalho de leitura, não um registro.

## O vocabulário de etiquetas é fechado

As etiquetas do campo `tags` não são livres: elas vivem no arquivo `_tags.yml`. Se a etiqueta
que você quer não está lá, você tem duas opções, e as duas são legítimas. A primeira é usar
uma que já exista. A segunda é propor a nova, acrescentando ao `_tags.yml` na mesma
contribuição e explicando na descrição por que ela faz falta.

Etiqueta usada uma vez só costuma ser sinal de que ela não era necessária.

## Confira antes de propor

Existe um programa que roda vinte e nove conferências sobre a wiki inteira. Ele é a diferença
entre uma contribuição que dá trabalho a alguém e uma que entra sozinha.

```bash
python <caminho-da-ferramenta>/scripts/validar_wiki.py --wiki-dir wiki --base-dir <raiz-do-acervo>
```

**Duas ressalvas honestas sobre isso.** A ferramenta que roda as conferências não está neste
repositório: ela é uma peça do ambiente do pesquisador. E a cópia em texto das leituras, que é
o que permite conferir se a passagem citada existe mesmo na página, também não está aqui,
porque inclui obra de terceiros protegida por direito autoral.

Na prática isso significa que **você não vai conseguir rodar a conferência de citação por
conta própria**. Faça o que dá: confira que o cabeçalho tem os seis campos obrigatórios, que
o nome do arquivo bate com o `slug`, que as etiquetas existem no `_tags.yml` e que os links
apontam para verbetes que existem. O resto é conferido na revisão.

Se a sua contribuição for reprovada por uma conferência que você não tinha como rodar, isso
não é falha sua. Você recebe o resultado e corrige.

## Como propor a sua contribuição

1. Crie uma cópia do projeto na sua conta, pelo botão de bifurcação do GitHub.
2. Crie um ramo com um nome que diga o que você fez, por exemplo `verbete-endogeneidade`.
3. Faça a alteração e escreva uma mensagem de registro explicando **por que**, e não só o quê.
4. Abra uma proposta de alteração. O formulário que aparece já traz a lista de conferência.

### Sobre a mensagem de registro

A mensagem boa responde a uma pergunta que o código não responde sozinho: por que esta
mudança precisava existir. "Acrescenta verbete de endogeneidade, que faltava para o capítulo
de inferência causal ligar a leitura de Angrist" é útil. "Atualiza arquivos" não é.

## O que costuma ser recusado

- Afirmação sobre o que um texto diz sem a passagem citada e a página.
- Passagem resumida ou parafraseada dentro do campo `excerpt`, que é reservado à citação
  literal.
- Verbete de conceito que só repete a definição de manual, sem dizer o que aquele conceito
  faz na disciplina.
- Etiqueta nova sem justificativa.
- Alteração grande misturando muitos assuntos, que fica impossível de revisar. Prefira várias
  propostas pequenas.

## Uma palavra sobre o tom

Os verbetes são escritos em português do Brasil, em prosa contínua. Não usamos lista de
tópicos dentro do corpo do verbete: o texto explica, ele não enumera. Termo técnico novo vem
com a explicação ao lado, na primeira vez que aparece.

Escrever assim custa mais tempo de quem escreve e economiza o de todos que vão ler depois.
