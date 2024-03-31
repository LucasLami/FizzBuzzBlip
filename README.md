# FizzBuzz Blip

## Description
FizzBuzz Blip est un jeu de logique basé sur les règles du jeu FizzBuzz, avec une variante supplémentaire appelée Blip. Le jeu peut être joué par deux joueurs ou plus.

## Comment jouer
Le jeu se déroule en plusieurs tours. À chaque tour, un nombre est affiché, et les joueurs doivent choisir parmi quatre options :

- **Fizz** : Si le nombre est divisible par 3, le joueur choisissant cette option marque un point.
- **Buzz** : Si le nombre est divisible par 5, le joueur choisissant cette option marque un point.
- **FizzBuzz** : Si le nombre est à la fois divisible par 3 et par 5, le joueur choisissant cette option marque un point.
- **Blip** : Si le nombre n'est pas divisible ni par 3 ni par 5, le joueur choisissant cette option marque un point.

Le joueur ayant le plus de points à la fin de la partie est déclaré vainqueur.

## Développement du projet
Ce projet a été développé en utilisant Python et la bibliothèque Tkinter pour l'interface graphique. Le jeu comporte également une intégration de la bibliothèque pygame pour la lecture de musique de fond.

## Installation
1. Assurez-vous d'avoir Python installé sur votre système.
2. Clonez ce dépôt sur votre machine.
3. Installez les dépendances en exécutant `pip install -r requirements.txt`.
4. Lancez le jeu en exécutant `python fizzbuzz_blip_gui.py`.

## Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, vous pouvez ouvrir une pull request ou signaler des problèmes en créant une issue.

## Auteurs
Ce jeu a été créé par [Lucas.L]. 

## Informations supplémentaires
Il y a aussi la version main jouable à partir du terminal !

Et pour avoir accès aux scores des joueurs, télécharger le fichier index + scores et suivre les instructions ci-dessous. (sinon regarder website.pdf)
1. Ouvrez une fenêtre de terminal ou de commande.
2. Naviguez jusqu'au répertoire contenant vos fichiers web à l'aide de la commande cd
3. Démarrez le serveur web local en exécutant la commande python -m http.server
4. Puis aller sur http://localhost:8000/
