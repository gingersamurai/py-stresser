HOST = gingersamurai@192.168.1.10

all: local_test deploy_test push clean

build: update
	python3 -m stresser

update: clean
	pip uninstall -y py-stresser
	python3 setup.py sdist
	pip install dist/*

local_test: update
	python3 test/test.py

deploy_test:
	ssh $(HOST) pip install py-stresser > /dev/null
	ssh $(HOST) stresser -h
	ssh $(HOST) pip uninstall -y py_stresser > /dev/null

push: update
	twine upload dist/*

clean:
	rm -rf dist py_stresser.egg-info
