---
schema_version: 1
type: text
slug: mariano-silva-2020
title: "Depois da “judicialização”: um mapa bibliográfico do Supremo"
status: complete
note_type: literaria
authors: [mariano-silva]
sessions:
  - id: s02-03
    role: obrigatoria
concepts:
  - id: protocolo-de-revisao
    evidence:
      - page: 2
        excerpt: "Para isso, adotei procedimentos que podem ser agrupados em quatro etapas."
      - page: 2
        excerpt: "Na primeira, defini quatro séries de termos de busca, para capturar textos em português, castelhano e inglês sobre o Supremo."
      - page: 2
        excerpt: "Excluí, portanto, dissertações, apresentações em congressos, relatórios, compilações de dados, resenhas, entrevistas, artigos de jornal e compêndios de normas"
      - page: 2
        excerpt: "Embora ela não esgote a literatura, a seleção sistemática e abrangente a torna representativa."
  - id: judicializacao
    evidence:
      - page: 1
        excerpt: "na última década, os estudos sobre o Supremo praticamente abandonaram o conceito"
sources:
  - path: "avaliacao/espelho_md/Desenhos e Técnicas Avançadas de Pesquisa 2026.2/Aula 02-03 - Problema de pesquisa e revisão bibliográfica replicável/MARIANO_SILVA_2020_Depois da judicialização_ um mapa bibliográfico do.md"
tags: [S02-03, protocolo-de-revisao, judicializacao]
verificacoes: []
---

# Depois da “judicialização”: um mapa bibliográfico do Supremo

O artigo pergunta como a “judicialização da política” deixou de agregar a produção das ciências
sociais sobre o Supremo Tribunal Federal e o que ocupou seu lugar. Responde com o que chama de
revisão bibliográfica sistemática: 148 textos publicados entre 1990 e 2021, classificados em oito
temas. Para esta wiki, o que importa é o **procedimento de construção do corpus**, porque é ele que torna o mapa conferível por outra pessoa. Ver
[[protocolo-de-revisao]].

## O mecanismo da seleção, em quatro etapas

O procedimento está na seção II, na p. 2 do espelho (p. 2/18 impressa), e funciona assim.

Na **primeira** etapa o autor fixa o vocabulário de busca antes de buscar: quatro séries de termos,
cada uma em português, castelhano e inglês, correspondendo a quatro modos de nomear o objeto (o
nome do Tribunal, o Judiciário como poder, a jurisdição constitucional e a própria judicialização).
A série multilíngue é o que impede que o recorte capture só a literatura brasileira, e a divisão em
quatro séries é o que impede que ele capture só quem já usa a palavra “judicialização”.

Na **segunda**, os termos vão ao [[mecanismo|mecanismo]] de busca do SciELO, restritos ao **título** do artigo, e
o resultado passa por dois filtros: janela de 1990 a 2021 e o critério substantivo de “análises
empíricas abrangentes do Supremo”. O que esse critério significa está em nota de rodapé, e não no
corpo: comentário de jurisprudência sai, e análise de julgamentos só entra se abranger mais de dez
deles.

Na **terceira**, o autor sai da base e entra na rede de referências: os mesmos termos são aplicados
às referências bibliográficas dos artigos já selecionados, para alcançar teses, livros, capítulos e
artigos que o SciELO não indexa. Aqui aparece a lista de exclusão por tipo de documento
(dissertações, congressos, relatórios, compilações de dados, resenhas, entrevistas, jornal e
compêndios de normas), e os filtros da segunda etapa são reaplicados.

Na **quarta**, a terceira etapa é reaplicada recursivamente sobre cada novo achado, “até esgotar
inteiramente a rede de referências”. É a bola de neve levada até a saturação declarada, e o
resultado é o número 148.

O desenho é, portanto, **base indexada mais bola de neve recursiva**, com critério de inclusão
substantivo (abrangência empírica), critério de exclusão por tipo documental e recorte temporal
explícito. O autor ainda separa a bibliografia básica (a que saiu do procedimento) da secundária (a
que entra por citação no argumento), e reserva as referências do corpo do texto à básica, o que
permite ao leitor saber, a cada menção, se está diante do corpus ou de fora dele.

## Onde o procedimento não é preciso, e isso é achado

O texto se declara “[[revisao-sistematica|revisão sistemática]]” já nas palavras-chave (p. 1 do espelho) e ancora o método
em Petticrew e Roberts, mas o que ele declara fica aquém do que um protocolo replicável exige. São
cinco imprecisões, todas verificáveis no próprio texto:

1. **Falta o rastro numérico entre etapas.** Só o total final aparece: 148. Não há quantos títulos
   a busca devolveu, quantos foram descartados em cada filtro nem por qual motivo. Sem esses
   números, ninguém consegue reproduzir o funil, apenas conferir o destino.
2. **Falta a data da busca e a expressão exata submetida à base.** As séries de termos estão
   listadas, mas não a sintaxe da consulta nem o dia em que foi rodada, e uma base viva devolve
   resultado diferente a cada mês.
3. **Uma base só, e só no título.** A segunda etapa usa exclusivamente o SciELO e só o campo de
   título. Texto cujo título não traz nenhum dos doze termos não entra por essa porta e depende de
   ser citado por alguém que entrou.
4. **O critério de inclusão está em nota, e é parcialmente arbitrário por confissão.** “Análises
   empíricas abrangentes” é operacionalizado como “mais de dez julgamentos”, em nota, com a
   justificativa de que incluir comentários jurisprudenciais tornaria a revisão inexequível. É
   critério de viabilidade, não de validade, e o autor o diz.
5. **A cobertura foi limitada pela pandemia, e a perda não é medida.** Outra nota registra que
   livros e capítulos ficaram restritos ao acervo das bibliotecas da USP e teses e artigos ao que
   estava disponível online. A restrição é declarada, o que é correto, mas não há estimativa do que
   ficou de fora.

Some-se um sexto ponto, que não é de busca e sim de análise: a classificação temática dos 148
textos na Tabela 1 (p. 7 do espelho) é atribuída a um único codificador, sem segunda codificação
nem medida de concordância. Como é dessa classificação que sai o argumento sobre a trajetória do
conceito, é ali que a replicabilidade fica mais frágil.

Nada disso reprova o artigo: ele declara mais procedimento do que a média dos ensaios
bibliográficos da área, e declara inclusive suas limitações. O que ele mostra, para efeito de
método, é a distância entre **declarar as etapas** e **entregar um protocolo que um terceiro possa
rodar de novo e chegar aos mesmos 148**. É essa distância que separa a revisão narrativa
disciplinada da revisão sistemática no sentido estrito.

## Por que este texto está na sessão

Ele é o par empírico do problema metodológico da aula: um mapa bibliográfico real, em português,
sobre um objeto jurídico, que permite ler o protocolo de revisão como decisão de pesquisa e não
como formalidade de seção de método. Serve também de contraste com os guias normativos da mesma
sessão, que dizem o que uma revisão deve reportar.
