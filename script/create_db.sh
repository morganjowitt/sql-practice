#!/bin/bash

set -a
source .env
set +a

docker run -d \
	--name postgres-db-sql \
	-e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v $VMOUNT_PATH:/var/lib/postgresql/data \
	-p $POSTGRES_PORT:5432 \
	postgres
