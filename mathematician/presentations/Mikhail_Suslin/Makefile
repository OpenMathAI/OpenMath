# Makefile for Erich Hecke beamer deck.
MAIN        = Mikhail_Suslin_zh
LATEXMK     = latexmk

.PHONY: all pdf clean distclean

all: pdf

pdf: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	-$(LATEXMK) -xelatex -synctex=0 -interaction=nonstopmode -f $(MAIN).tex
	-$(LATEXMK) -c $(MAIN).tex
	rm -f $(MAIN).{nav,snm,xdv}

clean:
	$(LATEXMK) -c $(MAIN).tex 2>/dev/null || true
	rm -f $(MAIN).{aux,log,toc,out,nav,snm,fls,fdb_latexmk,xdv} c.log

distclean: clean
	rm -f $(MAIN).pdf