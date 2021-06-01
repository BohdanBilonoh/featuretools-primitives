.PHONY : entry-point-test lint-fix lint-tests unit-tests

entry-point-test:
	python -c "from featuretools import custom_primitives"

.PHONY: clean
clean:
	find . -name '*.pyo' -delete
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	find . -name '*~' -delete
	rm -rf ./build
	rm -rf ./dist
	rm -rf ./nlp_primitives.egg-info

.PHONY: lint-fix
lint-fix:
	select="E225,E303,E302,E203,E128,E231,E251,E271,E127,E126,E301,W291,W293,E226,E306,E221"
	autopep8 --in-place --recursive --max-line-length=100 --select=${select} featuretools_primitives
	isort --recursive featuretools_primitives

.PHONY: lint-tests
lint-tests:
	flake8 feature_primitives
	isort --check-only featuretools_primitives

.PHONY: unit-tests
unit-tests:
	pytest --cache-clear --show-capture=stderr -vv

.PHONY: installdeps
installdeps:
	pip install --upgrade pip
	pip install -e .

.PHONY: installdeps-test
installdeps-test:
	pip install --upgrade pip
	pip install -e .
	pip install -r test-requirements.txt

.PHONY: featuretools_primitives
package_featuretools_primitives:
	python setup.py sdist
	$(eval PACKAGE=$(shell python setup.py --version))
	tar -zxvf "dist/featuretools_primitives-${PACKAGE}.tar.gz"
	mv "featuretools_primitives-${PACKAGE}" unpacked_sdist
