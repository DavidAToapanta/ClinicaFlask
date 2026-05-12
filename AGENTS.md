# AGENTS.md

## Python
- Python 3.14.4, virtualenv at `.venv/`
- Dependencies: Flask 3.1.3, Flask-SQLAlchemy, psycopg2, python-dotenv
- No `requirements.txt` / `pyproject.toml` — add manually when adding deps

## Project structure
Clean architecture:
- `app.py` — Flask entrypoint (run with `python app.py`)
- `base_datos/` — SQLAlchemy models (Cliente, Mascota, Veterinario, Consulta, Servicio, ConsultaServicio)
- `base_datos/__init__.py` — DB init con `_init_db(app)` que ejecuta `db.create_all()`
- `modelos/` — domain models (empty)
- `repositories/` — data access (empty)
- `services/` — business logic (empty)
- `routes/` — Flask blueprints (empty)

## Environment
- `.env` configured with PostgreSQL: `DB_USERNAME`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME=Veterinaria`
- Flask config: `FLASK_ENV=development`, `FLASK_DEBUG=True`
- `SECRET_KEY` in app.py with fallback: `os.getenv('SECRET_KEY', 'clave-secreet')`

## Development
- Run: `python app.py` (creates tables on startup)
- No test framework, no linter, no typechecker
- No git repo initialized