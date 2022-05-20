.PHONY: clean
clean:
	rm -rf dist
.PHONY: basic_build
basic_build: clean
	python -m app.build
.PHONY: pygmentize_css
pygmentize_css:
	pygmentize -S solarized-light -f html -a .codehilite > dist/styles.css
.PHONY: zip
zip:
	gzip -k -9 dist/*
.PHONY: build
build: basic_build pygmentize_css zip
.PHONY: rsync
rsync:
	rsync -rvz --progress -e 'ssh -p 57018' ./dist/* andrew@let-them.cyou:/srv/www/lt/andrew/tutorials/python
