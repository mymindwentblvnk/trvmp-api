PG_CONTAINTER=trvmp-postgres
PG_USER=postgres
PG_PASSWORD=postgres
PG_DATABASE=postgres

docker stop ${PG_CONTAINTER}
docker rm ${PG_CONTAINTER}
docker run --name ${PG_CONTAINTER} -p 5432:5432 -e POSTGRES_USER=${PG_USER} -e POSTGRES_PASSWORD=${PG_PASSWORD} -d ${PG_DATABASE}
export DATABASE_URL=postgresql://${PG_USER}:${PG_PASSWORD}@localhost/${PG_DATABASE}
sleep 1  # Needed to start Postgres entirely
source venv/bin/activate
pytest tests
docker stop ${PG_CONTAINTER}
docker rm ${PG_CONTAINTER}
deactivate
unset DATABASE_URL