VENV_PATH=venv
PYTHON=${VENV_PATH}/bin/python3

help:
	@echo "make help"
	@echo "       show this message"
	@echo "make venv"
	@echo "       prepare development environment"
	@echo "make lint"
	@echo "       run linter"
	@echo "make test"
	@echo "       run unit tests"
	@echo "make test_all"
	@echo "       run all tests (including system tests)"
	@echo "make run"
	@echo "       run project"
	@echo "make clean"
	@echo "       clean virtual environment"

# Requirements are in setup.py, so whenever setup.py is changed, re-run installation of dependencies.
venv: ${VENV_PATH}/bin/activate

${VENV_PATH}/bin/activate: setup.py
	test -d $(VENV_PATH) || python3 -m venv $(VENV_PATH)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -e .[test]
	${PYTHON} -m pip install -e .
	touch $@

lint: venv
	${PYTHON} -m pylint --disable=W0511,C0111 migration_agent

test: venv
	${PYTHON} -m pytest -k-system -s -v tests

test_all: venv
	${PYTHON} -m pytest -s -v tests

run: export FLASK_APP=migration_agent/migration_agent.py
run: export FLASK_ENV=development
run: export FLASK_DEBUG=0
run: venv
	${PYTHON} app.py

clean:
	rm -rf ${VENV_PATH}
	find . -iname "*.pyc" -delete

.DEFAULT: help
.PHONY: help venv lint test test_all run clean
