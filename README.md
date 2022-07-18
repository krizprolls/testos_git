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

## Faire un commit global
```sh
git add *
git commit -m "<message>"
```

## Créer fichier .gitignore
A la racine du projet, créer un fichier ".gitignore" dans lequel on inscrit les fichier ou dossier à ignorer lors du "git add *"


# Creer repo sur Github
Sur le compte github.com créer un nouveau repositorie
Suivre les instructions après la création du repo
```sh
echo "# testos_git" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/krizprolls/testos_git.git
git push -u origin main
```

## Push
ensuite dès qu'il y a modification
```sh
git add *
git commit -m "<messsage>"
git push
```
