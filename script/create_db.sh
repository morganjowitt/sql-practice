#!/bin/bash

set -a
source .env
set +a

docker run -d \
	--name postgres-db-sql \
	-e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
	-e PGDATA=$PGDATA_PATH \
	-v $VMOUNT_PATH:$DATA_PATH \
	-p $POSTGRES_PORT:5432 \
	postgres
