# Makefile for LIGO tutorial

# Create and configure environment with environment.yml

.PHONY: env

env:
	conda env update -n ligo --file environment.yml --prune || \
	conda env create -n ligo -f environment.yml


# Build HTML for the MyST site

.PHONY: html

html:
	myst build --html


# Clean up specified folders 

.PHONY: clean
clean:
	rm -rf figures/* audio/* _build/*