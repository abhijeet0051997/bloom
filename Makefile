GUINICORN_PORT = 8000
GUINICORN_WORKERS = 1
GUINICORN_TIME_OUT = 123

format:
	set -e
	isort --recursive  --force-single-line-imports app tests
	autoflake --recursive --remove-all-unused-imports --remove-unused-variables --in-place app tests
	black app tests
	isort --recursive app tests

lint:
	set -e
	set -x
	flake8 app --exclude=app/core/config.py
	mypy app
	black --check app --diff
	isort --recursive --check-only app

test:
	set -e
	set -x
	pytest -p no:warnings ./tests/*

test_with_coverage:
	set -e
	set -x
	coverage run -m pytest -p no:warnings ./tests/*


run_server:
	gunicorn --bind 0.0.0.0:8000 app.main:app --workers ${GUINICORN_WORKERS} --timeout ${GUINICORN_TIME_OUT} -k uvicorn.workers.UvicornWorker