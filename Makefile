
clean:
	-rm -rf build dist
	-find . -name '*.py[oc]' -exec rm {} \;

release: clean
	python setup.py sdist --formats=zip,gztar register upload

test:
	-unit2 discover

tags:
	ctags -R src setup.py

