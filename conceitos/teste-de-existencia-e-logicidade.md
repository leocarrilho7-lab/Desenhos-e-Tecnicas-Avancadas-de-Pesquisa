---
schema_version: 1
type: concept
slug: teste-de-existencia-e-logicidade
title: "Teste de Existência e Logicidade"
status: complete
note_type: permanente
zettel_id: "7c"
---

# Teste de Existência e Logicidade

Par de conferências que um modelo formal precisa passar antes que a condição derivada dele valha
como explicação, e que Mershon e Shvetsova (2019) executam em ordem no capítulo 5. A Existência
pergunta se a condição pode ser satisfeita por algum valor de parâmetro. A Logicidade pergunta
sob quais valores exatamente ela é satisfeita. A ordem não é estilística: é o conteúdo do
conceito.

## O mecanismo

O capítulo deriva, na p. 143 do espelho (p. 124 impressa), a condição para o Conselho recomendar
a mudança regulatória, uma restrição sobre o peso gama que os pescadores comerciais têm na
utilidade do órgão. Na p. 144 (p. 125) as autoras interrompem a conclusão e explicam por quê: é
crucial conferir a viabilidade da condição derivada antes de afirmar que é isso que se exige para
o Conselho querer recomendar, ou seja, é preciso garantir que o teste de Existência foi cumprido.

A conferência é sobre o domínio de parâmetros. Como gama tem de ser positivo por pressuposto, o
lado direito da expressão precisa ser positivo, e portanto o denominador também. Na mesma p. 144
(p. 125) vem o que está em jogo: o domínio pode ser vazio, e nesse caso a condição derivada seria
tautologia matemática. As autoras enunciam a consequência sem eufemismo: se fosse esse o caso,
a análise cairia no Quadrante 3 da figura 2.2, incapaz de explicar o comportamento observado sob
o conjunto de pressupostos adotado, por violação da Existência. A verificação, ainda na p. 144,
é aritmética e curta: como um dos termos é negativo e o outro positivo, a desigualdade necessária
pode ser satisfeita com facilidade.

Só então o texto avança. Na mesma p. 144 (p. 125) as autoras declaram estabelecida a Existência,
isto é, que é de fato possível, sob algumas condições, que o Conselho prefira recomendar mudança
à regulação vigente, e passam a se ocupar de cumprir o teste de Logicidade, que exige estabelecer
os limites de parâmetro para quando exatamente o Conselho preferiria mudança ao status quo.

## Por que a ordem importa

Uma condição pode ser formalmente correta e ainda assim vazia. Se o domínio em que ela vale for
vazio, todo o exercício de calibrar limites descreve um conjunto sem elementos, e o modelo
parecerá ter explicado um comportamento que ele nunca poderia gerar. A Logicidade sem a
Existência produz precisão sobre nada. É por isso que o cheque de domínio vem antes, e é por isso
que a p. 145 do espelho (p. 126) só apresenta as duas desigualdades juntas, a restrição sobre
gama e a condição de positividade, depois de as duas terem sido conferidas: ali as autoras
declaram estar no Quadrante 1 da figura 2.2 e prontas para traduzir os achados em hipóteses.

## O que a Logicidade entrega

Ela devolve sentido substantivo ao resultado, e não só o intervalo. Na p. 144 do espelho (p. 125)
as autoras leem a desigualdade em prosa: quanto maior for gama, maior precisa ser a probabilidade
de desaparecimento do Chinook para que o Conselho emita a recomendação. Isto é, quando os
pescadores comerciais são relativamente importantes para o Conselho, é preciso ameaça relativamente
grande à outra espécie para que o órgão se mova. Sem esse passo, a condição seria uma linha de
álgebra sem consequência observável, e a p. 145 (p. 126) não teria de onde tirar as hipóteses.

Uma ressalva sobre a letra dessa leitura, que não desfaz a citação acima. O símbolo que o espelho
grafa Ȥ é definido como sobrevivência duas vezes: na p. 128 do espelho (p. 109 impressa), "Ȥ
denotes the probability of Chinook  survival", e outra vez dentro do próprio Modelo 5.3, na p. 141
do espelho (p. 122 impressa), "Ȥ stands for the probability of the Chinook population’s survival".
Na p. 144 (p. 125) a prosa o nomeia ao contrário: "the cumulative probability of Chinook demise,
Ȥ(a), would need to be greater, the greater Ȗ is,  for the expression to hold". A letra da fonte
contradiz a definição que o próprio modelo deu ao símbolo. O que a álgebra pede é que seja maior o
ganho de sobrevivência ao trocar a tecnologia Agressiva pela Conservadora, isto é, a grandeza que a
p. 143 do espelho (p. 124 impressa) define como o aumento na probabilidade de sobrevivência do
Chinook quando a Conservadora substitui a Agressiva. A leitura substantiva das autoras sobrevive à
ressalva, porque um caminho para esse ganho crescer é a sobrevivência sob tecnologia Agressiva ser
menor, que é a ameaça de que a prosa fala. O que não sobrevive é o nome dado ao símbolo. A
releitura em termos dessa grandeza é reconstrução deste verbete, e não está escrita assim na fonte.

## De onde vem o corte interior no peso gama

Na p. 143 do espelho (p. 124 impressa) as autoras abreviam as duas diferenças que carregam a
condição: "Replacing for convenience the increase in the likelihood of Chinook  survival when
Conservative technology replaces Aggressive technology as  a = Ȥ(C) –  Ȥ(A), and the decline in
proﬁtability from switching to Conservative from Aggressive technology as b = L(C) –  L(A)". Com
isso a expressão 5.3.5 fica gama menor ou igual a 1 sobre (1 - Qb/a - l), com Q, l, a e b nas
grafias do espelho. A conferência de Existência, na p. 144 do espelho (p. 125 impressa), estabelece
que esse denominador pode ser positivo: "Note that b is the negative term as we deﬁned it,  while a
is positive. That implies that 1 –  Qb/a > 0, and so 1 –  Qb/a > l can  be easily satisﬁed."

O Modelo 5.1 já havia fixado o sinal de uma comparação entre esses mesmos objetos, quinze páginas
antes, na p. 128 do espelho (p. 109 impressa): "Given our assumptions about the relative importance
of the decline in the cost of pollock ﬁshing and about the relatively  low commercial ﬁshers’ loss
from marginally increasing the probability of Chinook depletion, ∆ub above is positive, that is,
Q(L(A)–L(C)) > –  [l(Ȥ(A) – Ȥ(C))]." Reescrita nas abreviações de 5.3, essa desigualdade diz que a
grandeza menos Qb/a supera l. Daí o denominador 1 - Qb/a - l ultrapassa 1, e o teto de gama, que é
1 sobre esse denominador, cai estritamente abaixo de 1.

**Essa passagem algébrica é reconstrução deste verbete, e não está escrita na fonte.** O que está
na fonte são as duas desigualdades citadas acima, a do Modelo 5.1 na p. 128 do espelho (p. 109
impressa) e a da conferência de Existência na p. 144 (p. 125), com as abreviações da p. 143
(p. 124) entre elas. Também é reconstrução a leitura de que gama não passa de 1, que vem da forma
da expressão 5.3.2, na p. 143 do espelho (p. 124 impressa), onde gama e o complemento dele repartem
a utilidade do Conselho entre os dois grupos de interessados; a fonte declara expressamente apenas
que gama precisa ser positivo, na p. 144 (p. 125).

O que a reconstrução mostra é por que a condição tem conteúdo. A Existência sozinha garante
denominador positivo, e denominador entre zero e um poria o teto acima de 1, isto é, acima de todo
valor que gama pode assumir: a condição existiria e nenhum peso seria excluído por ela. O
pressuposto herdado do Modelo 5.1 é o que empurra o denominador para cima de 1 e faz o corte cair
dentro do intervalo em que gama vive, separando os pesos que admitem a recomendação daqueles que
não a admitem.

É o caso concreto de que reusar resultado é reusar resultado com os pressupostos junto, regra que
[[conhecimento-extante-como-linha-de-base]] enuncia. A p. 142 do espelho (p. 123 impressa) já
declarava o encaixe, ao tratar os Modelos 5.1 e 5.2.2 como subjogos próprios do Modelo 5.3, e o que
o corte interior acrescenta é a direção em que a herança pesou: aqui o pressuposto importado deu
conteúdo à condição derivada, em lugar de esvaziar o domínio.

## Onde entra no resto do capítulo

O par de testes se aplica aqui à condição de recomendação do órgão descrito em
[[captura-regulatoria-oculta]], porque é essa condição que carrega o peso gama. E ele pesa
especialmente sobre quem usa modelo alheio como bloco, como descrito em
[[conhecimento-extante-como-linha-de-base]]: pressuposto herdado entra no domínio de parâmetros
junto com o resultado herdado, e domínio herdado sem conferência é o caminho curto para uma
condição que não pode ser satisfeita. Na conclusão, na p. 146 do espelho (p. 127), as autoras
registram o próprio capítulo como exemplo do que é cumprir as condições de Logicidade e
Existência no contexto de um modelo simples.
