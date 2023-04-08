.PHONY: help clean dev docs package test

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following make targets are available:"

setup:
	pip install --upgrade pip
	pip install coverage wheel

runtest:
	pip install -r ../requirements.txt
	echo "****************************************"
	echo "********** Current Versions! ***********"
	echo "****************************************"
	pip freeze
	echo "****************************************"
	echo "**********   Running Tests!   **********"
	echo "****************************************"
	coverage run runtests.py -v 2 --debug-mode
	coverage report -m
