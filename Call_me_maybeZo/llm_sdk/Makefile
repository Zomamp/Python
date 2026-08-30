MAIN = main_project.py

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
	UV_CACHE_DIR=$(CACHE_DIR) uv sync

run:
	UV_CACHE_DIR=$(CACHE_DIR) \
	HF_HOME=$(HF_CACHE_DIR) \
	uv run test.py

clean:
	rm -rf __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "__pycache__" -exec rm -rf {} +
