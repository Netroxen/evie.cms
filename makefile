QUART_APP=main:app
export QUART_APP

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
	flake8 --exclude=.tox

install:
	$(info "Running Evie Setup...")
	virtualenv .
	./bin/pip install -r requirements.txt

run:
	./bin/quart run

compile:
	$(info "Running Evie LESS Compile...")
	lessc --compress ./evie/static/less/custom.less ./evie/static/css/custom.min.css
