# Build the book:              make
# Build a single chapter:      make chapter CH=chapters/07-cnn-vision/04-transpose-convolution
# Remove auxiliary files:      make clean
MAIN = main

.PHONY: all chapter clean distclean

all:
	@rm -f includeonly.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN).tex

chapter:
	@test -n "$(CH)" || (echo "usage: make chapter CH=chapters/<part>/<chapter>"; exit 1)
	@echo '\includeonly{$(CH)}' > includeonly.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=chapter $(MAIN).tex
	@rm -f includeonly.tex

clean:
	latexmk -c $(MAIN).tex
	latexmk -c -jobname=chapter $(MAIN).tex
	find chapters -name '*.aux' -delete

distclean: clean
	rm -f $(MAIN).pdf chapter.pdf
