QUART_APP=main:app
export QUART_APP

EVIE_ENV=development
export EVIE_ENV

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf dist/
	@rm -rf build/
	@rm -rf README.rst
	@rm -rf .eggs/
	@rm -rf *.egg
	@rm -rf *.egg-info

isort:
	$(info "Sorting Python Imports...")
	sh -c "isort --skip-glob=.tox --recursive ./evie/"

lint:
	./bin/flake8 ./evie/ --exclude=.tox

install:
	$(info "Running Evie Setup...")
	virtualenv .
	./bin/pip install -r requirements.txt

run:
	$(info "Starting Evie...")
	./bin/quart run

compile:
	$(info "Running Compiling LESS Resources...")
	lessc --compress ./evie/static/less/custom.less ./evie/static/css/custom.min.css
