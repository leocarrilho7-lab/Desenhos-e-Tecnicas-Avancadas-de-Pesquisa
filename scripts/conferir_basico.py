#!/usr/bin/env python3
"""conferir_basico.py -- as conferencias que rodam sem o acervo.

POR QUE ESTE ARQUIVO EXISTE, e o que ele deliberadamente NAO faz.

A wiki tem um validador completo, com vinte e nove conferencias, e ele mora fora deste
repositorio, no ambiente do pesquisador. Ele depende de duas coisas que nao estao aqui: a
ferramenta em si e a copia em texto das leituras, que inclui obra de terceiros protegida por
direito autoral. A conferencia mais importante de todas, a que confirma se a passagem citada
existe mesmo naquela pagina, so roda la.

Sem este arquivo, o colaborador de fora nao teria conferencia NENHUMA para rodar, e
descobriria os erros so na revisao. Entao aqui esta o subconjunto que nao precisa do acervo:
estrutura do cabecalho, nome de arquivo, pasta, vocabulario de etiquetas e destino dos links.

O que ele NAO confere, e nao ha como conferir daqui: se a citacao e fiel, se a pagina esta
certa, se o excerto existe na fonte. Passar aqui NAO quer dizer que a contribuicao esta certa.
Quer dizer que ela nao tem os erros baratos. Guard que promete mais do que mede ensina a
confiar no lugar errado, e por isso este paragrafo esta aqui e nao num rodape.

Uso:
    python scripts/conferir_basico.py            # confere a wiki inteira
    python scripts/conferir_basico.py --autoteste
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):        # console de 8 bits nao pode abortar a saida
    sys.stdout.reconfigure(errors="backslashreplace")

RAIZ = Path(__file__).resolve().parent.parent
OBRIGATORIOS = ("schema_version", "type", "slug", "title", "status", "note_type")
PASTA_DO_TIPO = {"concept": "conceitos", "text": "textos", "author": "autores",
                 "session": "sessoes", "legislation": "legislacao", "julgado": "julgados"}
STATUS_VALIDO = ("stub", "complete")
_CABECALHO = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
_CAMPO = re.compile(r"^([a-z_]+):\s*(.*)$", re.M)
_LINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
_TAG_NO_YML = re.compile(r"^\s{0,2}-?\s*([A-Za-z0-9][\w.-]*)\s*:", re.M)


def cabecalho(texto: str) -> dict[str, str]:
    m = _CABECALHO.match(texto)
    return dict(_CAMPO.findall(m.group(1))) if m else {}


def etiquetas_declaradas(raiz: Path) -> set[str]:
    p = raiz / "_tags.yml"
    if not p.exists():
        return set()
    return {m.group(1) for m in _TAG_NO_YML.finditer(p.read_text(encoding="utf-8"))}


def verbetes(raiz: Path) -> list[Path]:
    """Varredura, nunca lista: pasta nova entra sozinha, sem ninguem cadastrar."""
    fora = {"docs", "scripts", ".git", ".github"}
    return sorted(p for p in raiz.rglob("*.md")
                  if not fora & set(p.relative_to(raiz).parts) and p.name != "README.md"
                  and p.name != "CONTRIBUTING.md")


def confere(raiz: Path) -> list[str]:
    falhas: list[str] = []
    arquivos = verbetes(raiz)
    slugs = {p.stem for p in arquivos}
    tags_ok = etiquetas_declaradas(raiz)
    for p in arquivos:
        rel = p.relative_to(raiz).as_posix()
        texto = p.read_bytes().decode("utf-8")
        cab = cabecalho(texto)
        if not cab:
            falhas.append(f"{rel}: sem cabecalho entre linhas de tres tracos")
            continue
        for campo in OBRIGATORIOS:
            if not cab.get(campo):
                falhas.append(f"{rel}: falta o campo obrigatorio '{campo}'")
        slug = cab.get("slug", "").strip().strip('"')
        if slug and slug != p.stem:
            falhas.append(f"{rel}: o slug '{slug}' nao bate com o nome do arquivo '{p.stem}'")
        tipo = cab.get("type", "").strip().strip('"')
        esperada = PASTA_DO_TIPO.get(tipo)
        if tipo and esperada is None:
            falhas.append(f"{rel}: tipo '{tipo}' desconhecido")
        elif esperada and p.parent.name != esperada:
            falhas.append(f"{rel}: tipo '{tipo}' deveria morar em '{esperada}/'")
        status = cab.get("status", "").strip().strip('"')
        if status and status not in STATUS_VALIDO:
            falhas.append(f"{rel}: status '{status}' nao e {' nem '.join(STATUS_VALIDO)}")
        for m in re.finditer(r"^tags:\s*\[(.*?)\]", texto, re.M):
            for t in (x.strip() for x in m.group(1).split(",")):
                if t and tags_ok and t not in tags_ok:
                    falhas.append(f"{rel}: etiqueta '{t}' nao existe em _tags.yml")
        for m in _LINK.finditer(texto):
            alvo = m.group(1).strip()
            if alvo not in slugs:
                falhas.append(f"{rel}: link [[{alvo}]] aponta para verbete que nao existe")
    return falhas


def _autoteste() -> int:
    """Cada caso nasce em par: um texto que precisa reprovar e um que nao pode reprovar."""
    import tempfile
    falhas: list[str] = []

    def checa(cond: bool, msg: str) -> None:
        if not cond:
            falhas.append(msg)

    bom = ('---\nschema_version: 1\ntype: concept\nslug: alfa\ntitle: "Alfa"\n'
           'status: complete\nnote_type: conceitual\ntags: [T1]\n---\n\n# Alfa\n')
    with tempfile.TemporaryDirectory() as d:
        r = Path(d)
        (r / "conceitos").mkdir()
        (r / "_tags.yml").write_text("T1:\n  descricao: teste\n", encoding="utf-8")
        (r / "conceitos" / "alfa.md").write_text(bom, encoding="utf-8")
        checa(confere(r) == [], f"verbete correto reprovou: {confere(r)}")

        (r / "conceitos" / "beta.md").write_text(bom.replace("slug: alfa", "slug: outro"),
                                                 encoding="utf-8")
        checa(any("nao bate com o nome" in f for f in confere(r)), "slug divergente passou")
        (r / "conceitos" / "beta.md").unlink()

        (r / "conceitos" / "gama.md").write_text(bom.replace("slug: alfa", "slug: gama")
                                                 .replace("[T1]", "[T9]"), encoding="utf-8")
        checa(any("nao existe em _tags.yml" in f for f in confere(r)), "etiqueta solta passou")
        (r / "conceitos" / "gama.md").unlink()

        (r / "conceitos" / "delta.md").write_text(
            bom.replace("slug: alfa", "slug: delta") + "\nliga para [[inexistente]].\n",
            encoding="utf-8")
        checa(any("nao existe" in f and "inexistente" in f for f in confere(r)),
              "link para verbete inexistente passou")
        (r / "conceitos" / "delta.md").unlink()

        (r / "textos").mkdir()
        (r / "textos" / "eps.md").write_text(bom.replace("slug: alfa", "slug: eps"),
                                             encoding="utf-8")
        checa(any("deveria morar em" in f for f in confere(r)), "tipo na pasta errada passou")
        (r / "textos" / "eps.md").unlink()

        (r / "conceitos" / "zeta.md").write_text(
            bom.replace("slug: alfa", "slug: zeta").replace("note_type: conceitual\n", ""),
            encoding="utf-8")
        checa(any("note_type" in f for f in confere(r)), "campo obrigatorio ausente passou")
        (r / "conceitos" / "zeta.md").unlink()

        checa(confere(r) == [], "sobrou falha depois de limpar os casos negativos")

    for f in falhas:
        print(f"  FALHOU: {f}")
    print("autoteste: " + ("VERDE" if not falhas else f"VERMELHO ({len(falhas)})"))
    return 1 if falhas else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--wiki-dir", default=str(RAIZ))
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()
    if a.autoteste:
        return _autoteste()
    raiz = Path(a.wiki_dir).resolve()
    falhas = confere(raiz)
    total = len(verbetes(raiz))
    if falhas:
        for f in falhas:
            print(f"  [FALHA] {f}")
        print(f"\n{len(falhas)} problema(s) em {total} verbetes. VERMELHO")
        return 1
    print(f"{total} verbetes conferidos, nenhum problema de estrutura. VERDE")
    print("Lembre: a fidelidade das citacoes NAO e conferida aqui, e sim na revisao.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
