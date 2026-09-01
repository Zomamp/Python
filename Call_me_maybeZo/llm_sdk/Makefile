MAIN = src/main.py

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
	@UV_CACHE_DIR=$(CACHE_DIR) uv sync

run:
	@UV_CACHE_DIR=$(CACHE_DIR) \
	HF_HOME=$(HF_CACHE_DIR) \
	uv run $(MAIN)

lint:
	@mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
	@flake8 --exclude=.venv,__pycache__,.mypy_cache .

lint-strict:
	@mypy --strict .
	@flake8 --exclude=.venv,__pycache__,.mypy_cache .

clean:
	@rm -rf __pycache__
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name "__pycache__" -exec rm -rf {} +
