# Demo git

## Création d'un projet avec Git
Dans votre dossier lancer la commande
```sh
git init
```

## Configuer GIT
```sh
git config --global user.name "<username>"
git config --global user.email "<mail_adress>"
```

## Créer un commit
Pour ajouter les modifs d'un fichier au commit
```sh
git add <nom_fichier>
git commit -m "<nom_commit>"
```

## Voir les fichiers modifiés, présents ou non dans le commit
```sh
git status
```

## Ouvrir fenêtre des branches
```sh
gitk
```