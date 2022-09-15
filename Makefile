HOST = gingersamurai@192.168.1.10

build: updateт
	python3 -m stresser

update: clean
	pip uninstall -y py-stresser
	python3 setup.py sdist
	pip install dist/py-stresser-2.0.0a12.tar.gz

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
