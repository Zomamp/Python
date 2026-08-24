MAIN = main_project.py

PROJECT_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
CACHE_DIR := $(PROJECT_DIR)/../cache
PYTHON = python3

.PHONY: all install run

all: run

install:
	UV_CACHE_DIR=$(CACHE_DIR) uv sync

run:
	UV_CACHE_DIR=$(CACHE_DIR) uv run $(MAIN)

clean:
	rm -rf __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "__pycache__" -exec rm -rf {} +

debug:
	uv run ${PYTHON} -m pdb
