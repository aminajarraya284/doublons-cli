# Doublons CLI

Retrouvez les fichiers au contenu identique dans un dossier et ses sous-dossiers, même quand leurs noms diffèrent. L’outil affiche les chemins par groupe et laisse tous les fichiers en place.

## Utilisation

Avec Python 3.11 ou une version ultérieure, ouvrez un terminal dans le dossier du projet et lancez cette commande en remplaçant le chemin entre guillemets par celui de votre dossier.

```sh
python doublons.py "chemin/vers/mes fichiers"
```

## Exemple de résultat

```text
Groupe 1 (2 fichiers)
  photos/portrait.jpg
  photos/archives/copie.jpg
```

Le programme regroupe les fichiers par taille, puis compare les empreintes SHA-256 des candidats. Il ignore les liens symboliques. Les erreurs de lecture apparaissent dans le terminal et donnent un code de sortie de 1.
