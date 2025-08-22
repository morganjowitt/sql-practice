#!/bin/bash

# Nom du conteneur Docker
CONTAINER_NAME="postgres-db-sql"
echo "Démarrage du conteneur..."
docker start $CONTAINER_NAME
