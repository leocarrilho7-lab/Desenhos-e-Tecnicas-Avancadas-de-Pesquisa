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
