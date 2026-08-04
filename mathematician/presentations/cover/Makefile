# Makefile for OpenMath Cover template
#
# Usage:
#   make            build the PDF
#   make pdf        same as above
#   make clean      remove intermediate files
#   make distclean  remove generated PDF

MAIN        = OpenMath_Cover
LATEXMK     = latexmk

.PHONY: all pdf clean distclean

all: pdf

pdf: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	$(LATEXMK) -xelatex -synctex=0 -interaction=nonstopmode $(MAIN).tex || \
	  (rm -f $(MAIN).fdb_latexmk && $(LATEXMK) -xelatex -synctex=0 -interaction=nonstopmode -f $(MAIN).tex)
	$(LATEXMK) -c $(MAIN).tex
	rm -f $(MAIN).{nav,snm,xdv}

clean:
	$(LATEXMK) -c $(MAIN).tex 2>/dev/null || true
	rm -f $(MAIN).{aux,log,toc,out,nav,snm,fls,fdb_latexmk,xdv} c.log

distclean: clean
	rm -f $(MAIN).pdf
