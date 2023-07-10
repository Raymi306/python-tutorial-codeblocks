.PHONY: default
default: build

.PHONY: clean
clean:
	rm -rf dist
.PHONY: lint
lint:
	pylint app
.PHONY: init_dist_dir
init_dist_dir:
	mkdir -p dist
.PHONY: basic_build
basic_build: clean init_dist_dir
	python -m app
.PHONY: basic_build_new_internal_links
basic_build_new_internal_links: clean init_dist_dir
	python -m app --new-internal-links
.PHONY: pygmentize_css
pygmentize_css:
	pygmentize -S solarized-light -f html -a .codehilite > dist/styles.css
.PHONY: zip
zip:
	gzip -k -9 dist/*
.PHONY: build
build: lint basic_build pygmentize_css zip
.PHONY: build_new_internal_links
build_new_internal_links: lint basic_build_new_internal_links pygmentize_css zip
.PHONY: rsync
rsync:
	rsync -rvz --progress -e 'ssh -p 57018' ./dist/* andrew@let-them.cyou:/srv/www/lt/andrew/tutorials/python
