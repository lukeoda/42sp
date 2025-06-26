#!/bin/bash
NETWORK_NAME="my_network_ex06"
DB_CONTAINER_NAME=postgres_db
API_CONTAINER_NAME=my_api_app

export SENHA_BANCO=lucas123

if docker ps -a --format '{{.Names}}' | grep -q "$API_CONTAINER_NAME"; then
    docker stop "$API_CONTAINER_NAME" &>/dev/null
    docker rm "$API_CONTAINER_NAME" &>/dev/null
fi

if docker ps -a --format '{{.Names}}' | grep -q "$DB_CONTAINER_NAME"; then
    docker stop "$DB_CONTAINER_NAME" &>/dev/null
    docker rm "$DB_CONTAINER_NAME" &>/dev/null
fi


if ! docker network ls | grep -q "$NETWORK_NAME"; then
  docker network create "$NETWORK_NAME"
fi

docker run --name $DB_CONTAINER_NAME \
--network $NETWORK_NAME \
-v postgres-data:/var/lib/postgresql/data \
-p 5432:5432 \
-e POSTGRES_DB=ningipoints \
-e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=${SENHA_BANCO} \
-d postgres

docker build -t api_lkenji .

docker run --name $API_CONTAINER_NAME \
--network $NETWORK_NAME \
-p 8080:8080 \
-e POSTGRES_SENHA=${SENHA_BANCO} \
-e POSTGRES_USER=postgres \
-e POSTGRES_DB=ningipoints \
-e POSTGRES_HOST=postgres_db \
-e POSTGRES_PORT=5432 \
-d api_lkenji 

