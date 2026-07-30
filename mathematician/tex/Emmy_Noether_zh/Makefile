# Auto-generated 中文版 per-person Makefile.
NAME := Emmy_Noether_zh
TEX  := $(NAME).tex
PDF  := $(NAME).pdf

.PHONY: all pdf build clean distclean

all: pdf

build: $(PDF)

pdf: $(PDF)
	@$(MAKE) --no-print-directory clean

$(PDF): $(TEX) body.tex metadata.tex ../common/preamble_zh.tex
	latexmk -xelatex -interaction=nonstopmode -halt-on-error $(TEX)

clean:
	@latexmk -c $(TEX) >/dev/null 2>&1 || true
	@rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz *.xdv

distclean: clean
	rm -f $(PDF)
