# Setup

- Run `poetry install`
- Create a `db.sqlite3` file at root
- Copy `env.example` to `.env` providing your values

# Using uvicorn

- Run `uvicorn entrypoint.main:app --reload`

# Tests

- Run `python -m pytest`
