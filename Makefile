.PHONY: setup jupyter gateway test clean

# Initializes the dev environment
setup:
	python -m pip install -e .[dev]

# Launches the sandbox for Phase 1 & 2
jupyter:
	jupyter lab --no-browser --port=8888

# Runs the Week 6 Capstone FastAPI server
gateway:
	uvicorn 03_capstone_wiki_engine.gateway_api.main:app --reload --host 0.0.0.0 --port 8000

# Runs all evaluations and unit tests
test:
	pytest 03_capstone_wiki_engine/tests/ -v

# Cleans up the repo
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf .venv/
