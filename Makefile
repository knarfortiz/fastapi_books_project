# Project
env:
	python3 ./venv/bin/activate
i:
	pip install -r requirements.txt

# FastAPI
run:
	fastapi dev main.py

# Ruff commands
rc:
	ruff check 
rf:
	ruff format
rx:
	ruff check --fix