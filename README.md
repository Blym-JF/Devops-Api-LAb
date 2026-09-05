# DevOps Docker API Lab
## Objectif
Créer et conteneuriser une API Flask minimale, puis vérifier son état de santé via un
## Fonctionnalités- `GET /` : message d’accueil- `GET /health` : état de santé de l’API- `GET /version` : version et environnement d’exécution
## Technologies- Python 3- Flask- Docker- Docker Compose- Git et GitHub
## Architecture
```text
Client (curl ou navigateur)
|
v
Port 8080 de la machine
|
v
Conteneur Docker : API Flask
