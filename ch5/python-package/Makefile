
deploy-testpypi:
	pandoc --from=markdown --to=rst README.md -o README.rst
	python setup.py check --restructuredtext --strict --metadata
	rm -rf dist
	python setup.py sdist
	twine upload dist/*
	rm -rf README.rst