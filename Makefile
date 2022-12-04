.PHONY: conda-env setup requirements test
.DEFAULT_GOAL := setup
-include .env

conda-env:
	mamba env create --prefix ./env --no-default-packages

setup:
	pip install pip-tools
	pip-sync requirements.txt
	pip install -e .

requirements:
	pip-compile requirements.in -o requirements.txt --resolver=backtracking -v
	pip-sync requirements.txt
	pip install -e .

test:
	pytest
