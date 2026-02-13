# Medicalka App

Backend API project built with Django REST Framework, PostgreSQL, Celery, and Redis.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-API-red?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-4169E1?logo=postgresql&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-Tasks-37814A?logo=celery&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-Queue-DC382D?logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)

## Tech Stack
- Python 3.12+
- Django 6
- Django REST Framework
- PostgreSQL 14+
- Celery + Redis
- Docker + Docker Compose
- Swagger/ReDoc (drf-yasg)

## Project Structure
- `apps/user` - registration, login, profile, OTP verify
- `apps/main/post` - post CRUD and background cleanup task
- `apps/main/comment` - comment CRUD per post
- `apps/main/like` - like/unlike per post
- `config` - Django settings, URLs, WSGI/ASGI, Celery app

## API Documentation
After startup:
- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`
- Postman collection/docs with example responses: [Link](https://www.postman.com/project-x-001/workspace/medicalka-api-docs)

## Environment Variables
Create `.env` in the project root.

Recommended example:

```env
# DB (local non-docker mode)
POSTGRES_NAME=medicalka_db
POSTGRES_USER=medicalka_user
POSTGRES_PASSWORD=medicalka_123
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# DB (docker mode)
POSTGRES_NAME_DOCKER=medicalka_db
POSTGRES_USER_DOCKER=medicalka_user
POSTGRES_PASSWORD_DOCKER=medicalka_123
POSTGRES_HOST_DOCKER=db
POSTGRES_PORT=5432

# Choose backend db: sqlite | postgresql | postgresql_docker
BACKEND_DB=sqlite

# Email/OTP
EMAIL_FROM=you@example.com
EMAIL_HOST_USER=you@example.com
EMAIL_HOST_PASSWORD=your_app_password

# Celery/Redis
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
```

## Local Setup (Without Docker)

1. Create and activate virtual environment:
```bash
python3.12 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Configure `.env`:
- For SQLite quick run: set `BACKEND_DB=sqlite`
- For PostgreSQL: set `BACKEND_DB=postgresql` and fill `POSTGRES_*`

4. Run migrations and collect static files:
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

5. (Optional) Create superuser:
```bash
python manage.py createsuperuser
```

SQLite quick-check default admin (if using existing local SQLite DB):
- username: `admin`
- password: `med_pass_123`

6. Run server:
```bash
python manage.py runserver
```

7. (Optional) Run Celery worker and beat in separate terminals:
```bash
celery -A config.celery:app worker -l info
celery -A config.celery:app beat -l info
```

## Background Cleanup Schedule (Celery Beat)
These tasks run automatically to keep the database clean.

- Timezone: `Asia/Tashkent`
- Unverified users cleanup
  - Task: `apps.user.tasks.delete_expired_users_task`
  - Runs: every Sunday at `00:00`
- Old posts cleanup
  - Task: `apps.main.post.tasks.delete_expired_posts_task`
  - Runs: every `30` days

## Docker Setup

1. Ensure Docker is installed and running.

2. Build and start all services:
```bash
docker compose up --build
```

This starts:
- `web` (Django + Gunicorn)
- `db` (PostgreSQL)
- `redis`
- `worker` (Celery worker)
- `beat` (Celery beat scheduler)

3. Application URLs:
- API base: `http://localhost:8000/`
- Admin: `http://localhost:8000/admin/`
- Swagger: `http://localhost:8000/swagger/`

4. Stop services:
```bash
docker compose down
```

5. Stop and remove volumes (clean DB):
```bash
docker compose down -v
```

## Running Tests

Automated test files currently exist but are placeholders (no implemented test cases yet):
- `apps/user/tests.py`
- `apps/main/post/tests.py`
- `apps/main/comment/tests.py`
- `apps/main/like/tests.py`

Command to run test discovery:
```bash
python manage.py test
```

Docker:
```bash
docker compose run --rm web python manage.py test
```

## Manual Test Checklist (For Interview)

1. Open Swagger at `http://localhost:8000/swagger/`.
2. Register user: `POST /user/auth/register/`.
3. Verify account (OTP flow): `POST /user/auth/verify/`.
4. Login: `POST /user/auth/login/` and copy JWT token.
5. Click `Authorize` in Swagger and paste `Bearer <token>`.
6. Create post via `/posts/`.
7. List/update/delete post via `/posts/` endpoints.
8. Create/list comments via `/posts/{post_id}/comment/`.
9. Like/unlike via `/posts/{post_id}/like/`.
10. Check profile endpoints:
- `GET /user/auth/me/`
- `PUT/PATCH /user/users/me/`

> Optional interviewer shortcut: add `?fake_verify=true` to register request to skip sending OTP email and simulate verification flow.
   Example: `POST /user/auth/register/?fake_verify=true`

## Key Routes Summary
- `POST /user/auth/register/`
- `POST /user/auth/verify/`
- `POST /user/auth/login/`
- `GET /user/auth/me/`
- `PUT/PATCH /user/users/me/`
- `GET /user/all/`
- `GET/POST /posts/`
- `GET/PUT/PATCH/DELETE /posts/{id}/`
- `GET/POST /posts/{post_id}/comment/`
- `GET/PUT/PATCH/DELETE /posts/{post_id}/comment/{id}`
- like router under `/posts/{post_id}/like/`

## Notes For Interviewer
- Project includes async background processing with Celery and Redis.
- API docs are available through Swagger/ReDoc for quick verification.
- Docker setup is production-like (Gunicorn + Postgres + Redis + worker + beat).
- Current test suite structure is prepared, but test cases still need implementation.
- Credentials/secrets should be provided through environment variables only.

## Common Troubleshooting
- Admin page without CSS/JS:
  - Ensure `collectstatic` has run (already included in Docker startup).
- Django install error with Python 3.11:
  - Use Python 3.12+ (Django 6 requirement).
- DB connection issues:
  - Confirm `BACKEND_DB` and matching DB env variables.
- Celery not processing:
  - Verify `redis` service is healthy and `REDIS_HOST=redis` in Docker.
- `celery -A config.celery:app worker -l info` fails with `ModuleNotFoundError: No module named 'dotenv'`:
  - Activate your project virtual environment first: `source venv/bin/activate`
  - Reinstall dependencies: `pip install -r requirements.txt`
  - Confirm package exists: `pip show python-dotenv`
  - Then rerun worker command.

## AI Attribution
- This `README.md` was fully created by AI but has undergone a thorough author check.
- Docker-related parts were created by the project author with partial AI assistance because Time was deficit.
