
clean:
	-rm -rf build dist
	-find . -name '*.py[oc]' -exec rm {} \;
.PHONY: clean

release: clean
	python setup.py sdist --formats=zip,gztar register upload
.PHONY: release

test:
	-unit2 discover
.PHONY: test

tags:
	ctags -R pyong setup.py
.PHONY: tags

