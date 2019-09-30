QUART_APP=main:app
export QUART_APP

EVIE_ENV=development
export EVIE_ENV

clean:
	# Find Files
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*.map' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	# Remove Dirs
	@rm -rf dist/
	@rm -rf build/
	@rm -rf .eggs/
	@rm -rf *.egg
	@rm -rf *.egg-info
	# Remove DB
	@find ./var/filestorage/ -name 'Data.fs*' -exec rm -f {} \;


isort:
	$(info "Sorting Python Imports...")
	sh -c "isort --skip-glob=.tox --recursive ./evie/"

lint:
	./bin/flake8 ./evie/ --exclude=.tox

install:
	$(info "Running Evie Setup...")
	virtualenv -p python3 .
	./bin/pip install -r requirements.txt

run:
	$(info "Starting Evie...")
	./bin/quart run

compile:
	$(info "Running Compiling LESS Resources...")
	lessc --compress ./evie/static/less/custom.less ./evie/static/css/custom.min.css
