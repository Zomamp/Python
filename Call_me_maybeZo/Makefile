MAIN = src/__main__.py

PROJECT_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
CACHE_DIR := $(PROJECT_DIR)/../cache
PYTHON = python3
HF_CACHE_DIR := $(PROJECT_DIR)/../huggingface-cache
###################################################
# Addding some folder for this project
###################################################


.PHONY: all install run

all: run

install:
	@UV_CACHE_DIR=$(CACHE_DIR) uv add torch transformers huggingface-hub pydantic llm-sdk mypy flake8
	@UV_CACHE_DIR=$(CACHE_DIR) uv pip install pydantic mypy flake8
	@UV_CACHE_DIR=$(CACHE_DIR) uv sync

lint:
	@python3 -m mypy src --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
	@python3 -m flake8 --exclude=.venv,__pycache__,.mypy_cache src

lint-strict:
	@python3 -m mypy --strict src
	@python3 -m flake8 --exclude=.venv,__pycache__,.mypy_cache src

run:
	@UV_CACHE_DIR=$(CACHE_DIR) \
	HF_HOME=$(HF_CACHE_DIR) \
	uv run $(MAIN)

clean:
	@rm -rf __pycache__
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name "__pycache__" -exec rm -rf {} +

help:
	@echo "\033[035mmake install\033[0m is for installation, the cache and huggingface is already in the folder of actual folder, don't worry about it"
	@echo "\033[035mmake lint\033[0m is for the managing of the  project , using flake8 and mypy"
	@echo "\033[035mmake lint-strict \033[0m Same as below but more strict"
	@echo "\033[035mmake run \033[0m To run the project"
	@echo "\033[035mmake \033[0m If you just do make, the program run"