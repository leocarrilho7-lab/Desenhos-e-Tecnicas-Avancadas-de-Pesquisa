# Desenhos e Técnicas Avançadas de Pesquisa, wiki

**Site: https://leocarrilho7-lab.github.io/Desenhos-e-Tecnicas-Avancadas-de-Pesquisa/**

Wiki de leitura da disciplina obrigatória de doutorado do Programa de Pós-graduação em Direito da
Regulação da FGV, 2026.2, 45 horas. No site os `[[wikilinks]]` viram links de verdade, e há busca e
grafo; aqui no repositório está a fonte em markdown, que é o que se revisa por pull request.

Cada afirmação sobre um texto vem ancorada em página de um espelho do PDF, e um script confere o
excerto contra aquela página. Os espelhos, que trazem o texto integral das obras, **não** estão
neste repositório.

Referencia rapida. **Nao e documento normativo**: quem manda e a `spec.md` deste projeto e o
`SKILL.md` da `wikify`.

## Tipos de no

`author` · `text` · `concept` · `session` · `legislation` · `julgado`, um arquivo por no em
`wiki/<pasta>/<slug>.md`. **Tag** e vocabulario controlado em `wiki/_tags.yml`.

Todo no declara `schema_version`, `type`, `slug`, `title`, `status` e `note_type`.

## Ligacao

`[[slug]]` num verbete de CONCEITO gera aresta `relaciona_se_com`, simetrica. Em qualquer outro
lugar e navegação. Relacao com significado vai no frontmatter, nunca só no corpo.

## Antes de entregar

```
python <skill>/scripts/conferir_espelho.py --corpus <espelhos>
python <skill>/scripts/validar_wiki.py --wiki-dir wiki --base-dir <raiz do corpus>
```

Este arquivo não entra no grafo: o carregador ignora `README.md` de propósito, para não forcar um
tipo de no artificial.

## Quer colaborar

Leia o [guia de colaboração](CONTRIBUTING.md). Ele explica os tipos de verbete, o formato do
cabecalho, as duas maneiras de ligar verbetes e o que costuma ser recusado, em portugues e
sem pressupor que você já conheca o projeto.

Antes de propor qualquer coisa, rode a conferência que dispensa o acervo:

```bash
python scripts/conferir_basico.py
```

Ela confere estrutura, e não conteúdo. **A fidelidade das citações não e conferida por ela**,
porque depende da copia em texto das leituras, que não esta neste repositório por causa de
direito autoral. Isso fica para a revisão, e não e falha sua.

## Licenca

Creative Commons Atribuicao-NaoComercial-CompartilhaIgual 4.0 Internacional, a mesma do
projeto Disaster Law and Policy. O arquivo [LICENSE](LICENSE) traz o texto integral e a
ressalva que importa: as passagens citadas de obras de terceiros continuam dos seus autores,
e a licença cobre o que foi escrito aqui.
