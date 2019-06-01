QUART_APP=main:app
export QUART_APP

QUART_DEBUG=False
export QUART_DEBUG

TEMPLATES_AUTO_RELOAD=True
export TEMPLATES_AUTO_RELOAD

isort:
	sh -c "isort --skip-glob=.tox --recursive ./evie/"

lint:
	flake8 --exclude=.tox

install:
	virtualenv .
	./bin/pip install -r requirements.txt

run:
	./bin/quart run
