#!/bin/bash

# Nom du conteneur Docker
CONTAINER_NAME="postgres-db-sql"

# Vérifie si le conteneur existe
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Arrêt du conteneur $CONTAINER_NAME..."
    docker stop $CONTAINER_NAME
    echo "Conteneur arrêté avec succès."
else
    echo "Aucun conteneur nommé $CONTAINER_NAME en cours d'exécution."
fi
