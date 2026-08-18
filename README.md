# Desenhos e Técnicas Avançadas de Pesquisa, wiki

Referencia rapida. **Nao e documento normativo**: quem manda e a `spec.md` deste projeto e o
`SKILL.md` da `wikify`.

## Tipos de no

`author` · `text` · `concept` · `session` · `legislation` · `julgado`, um arquivo por no em
`wiki/<pasta>/<slug>.md`. **Tag** e vocabulario controlado em `wiki/_tags.yml`.

Todo no declara `schema_version`, `type`, `slug`, `title`, `status` e `note_type`.

## Ligacao

`[[slug]]` num verbete de CONCEITO gera aresta `relaciona_se_com`, simetrica. Em qualquer outro
lugar e navegacao. Relacao com significado vai no frontmatter, nunca so no corpo.

## Antes de entregar

```
python <skill>/scripts/conferir_espelho.py --corpus <espelhos>
python <skill>/scripts/validar_wiki.py --wiki-dir wiki --base-dir <raiz do corpus>
```

Este arquivo nao entra no grafo: o carregador ignora `README.md` de proposito, para nao forcar um
tipo de no artificial.

## Quer colaborar

Leia o [guia de colaboracao](CONTRIBUTING.md). Ele explica os tipos de verbete, o formato do
cabecalho, as duas maneiras de ligar verbetes e o que costuma ser recusado, em portugues e
sem pressupor que voce ja conheca o projeto.

Antes de propor qualquer coisa, rode a conferencia que dispensa o acervo:

```bash
python scripts/conferir_basico.py
```

Ela confere estrutura, e nao conteudo. **A fidelidade das citacoes nao e conferida por ela**,
porque depende da copia em texto das leituras, que nao esta neste repositorio por causa de
direito autoral. Isso fica para a revisao, e nao e falha sua.

## Licenca

Creative Commons Atribuicao-NaoComercial-CompartilhaIgual 4.0 Internacional, a mesma do
projeto Disaster Law and Policy. O arquivo [LICENSE](LICENSE) traz o texto integral e a
ressalva que importa: as passagens citadas de obras de terceiros continuam dos seus autores,
e a licenca cobre o que foi escrito aqui.
