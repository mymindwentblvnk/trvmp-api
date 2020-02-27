#!/usr/bin/env bash
PG_CONTAINTER=trvmp-postgres
PG_USER=postgres
PG_PASSWORD=postgres
PG_DATABASE=postgres

PG_SPINUP_TIME=2


docker run --name ${PG_CONTAINTER} -p 5432:5432 -e POSTGRES_USER=${PG_USER} -e POSTGRES_PASSWORD=${PG_PASSWORD} -d ${PG_DATABASE}
export DATABASE_URL=postgresql://${PG_USER}:${PG_PASSWORD}@localhost/${PG_DATABASE}
echo "Waiting ${PG_SPINUP_TIME} seconds to spin up Postgres..."
sleep ${PG_SPINUP_TIME}  # Needed to start Postgres entirely
pytest tests
docker stop ${PG_CONTAINTER}
docker rm ${PG_CONTAINTER}
deactivate
unset DATABASE_URL