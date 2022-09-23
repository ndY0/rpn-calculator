#   CALCULATRICE RDN

## Description

Ce projet est une implémentation simple et à complèter d'une calculatrice en notation polonaise inversée
Elle est exposé en tant qu'api http aux utilisateur.
la consommation de l'api est décrite dans le fichier `rpn_openapi.yaml` joint à la racine de ce projet

### spécification technique :

- langage: Python 3.10
- framework: flask
- base de donnée: redis 7.0

##  Prérequis

- docker installé, en cours d'exécution
- outil cli docker-compose disponible
- outil cli make disponible

## Installation

étapes :

- initialiser la configuration du projet avec la commande `make init`
- modifier à la convenance les fichiers .env générés
- le serveur de développement se démarre avec `make start`, et se stop avec `make stop`

le serveur est accessible sur le localhost, sur le port 8080

## Choix constructifs

Langage et framework : le sujet proposait d'utiliser le langage python, ce qui me semblait adapté pour un projet de cette envergure, sans spécifiquement d'attente de performance dans spécifiques.
Le framework flask est un micro-framework, idéal pour minimiser les dépendances embarqués sur de petits projet, m'a paru adapté également.

J'ai pris la décision, afin de persister les structures de données de ce projet, une base de donnée redis. Redis a l'avantage de mettre à disposition des types de données assez proches de ceux que j'estimais utiliser dans l'application (sets pour gérer les piles existantes, listes liées pour les données des piles), j'ai donc décidé de construire l'application autour de cette architecture de base.
Redis a également l'avantage d'être très performante, étant une base de donnée en RAM.

Le projet est conteneurisé grace à l'outil de conteneurisation docker, l'orchestration du projet est assurée par l'outi docker-compose. j'ai fait ce choix afin de minimiser les prérequis d'installation du projet, et de faciliter l'industrialisation du projet par la suite.