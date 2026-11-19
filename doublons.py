"""Repère les fichiers identiques dans une arborescence."""

import argparse
import hashlib
import os
import sys
from collections import defaultdict
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dossier", type=Path, help="dossier à analyser")
    dossier = parser.parse_args().dossier
    if not dossier.is_dir():
        parser.error("indiquez un dossier existant")

    erreurs = []
    tailles = defaultdict(list)
    for racine, _, noms in os.walk(dossier, onerror=erreurs.append):
        for nom in noms:
            chemin = Path(racine) / nom
            try:
                if not chemin.is_symlink() and chemin.is_file():
                    tailles[chemin.stat().st_size].append(chemin)
            except OSError as exc:
                erreurs.append(exc)

    groupes = []
    for chemins in tailles.values():
        if len(chemins) < 2:
            continue
        empreintes = defaultdict(list)
        for chemin in chemins:
            try:
                with chemin.open("rb") as fichier:
                    empreinte = hashlib.file_digest(fichier, "sha256").digest()
                empreintes[empreinte].append(chemin)
            except OSError as exc:
                erreurs.append(exc)
        groupes.extend(sorted(groupe) for groupe in empreintes.values() if len(groupe) > 1)

    for numero, groupe in enumerate(sorted(groupes), 1):
        print(f"Groupe {numero} ({len(groupe)} fichiers)")
        for chemin in groupe:
            print(f"  {chemin}")
    if not groupes:
        print("Aucun doublon détecté parmi les fichiers analysés.")
    for erreur in erreurs:
        print(erreur, file=sys.stderr)
    return int(bool(erreurs))


if __name__ == "__main__":
    sys.exit(main())
