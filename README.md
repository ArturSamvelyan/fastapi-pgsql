# Fastapi PostgreSQL project template.
## Installation

Install all dependencies by **pip**:

```shell
pip install -r requirements.txt
```

or install all dependencies by **pipenv**:

```shell
pipenv install

# and then activate virtual environment
pipenv shell
```

## Development
1) `docker-compose -f docker-compose-dev.yml up -d`.
2) `docker exec -it tts_api_pgsql_dev psql -U tts_service_user -d tts_db -f /misc/createdb.sql`
3) Go to `http://localhost:8000/docs`.

## Production
1) `docker-compose -f docker-compose.yml up -d`.
2) `docker exec -it tts_api_pgsql_dev psql -U tts_service_user -d tts_db -f /misc/createdb.sql`
3) Go to `http://localhost:8000/docs`.
