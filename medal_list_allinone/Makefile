# Makefile for the mathematics-awards list documents.
#
# Usage:
#   make            build all PDFs
#   make cross      build cross-reference PDF (cross_ref/)
#   make beamer     build the Fields beamer PDF (fields_beamer/)
#   make wolf       build the Wolf Prize beamer PDF (wolf_beamer/)
#   make abel       build the Abel Prize beamer PDF (abel_beamer/)
#   make clean      remove intermediate files
#   make distclean  remove generated PDFs

CROSS_DIR   = cross_ref
BEAMER_DIR  = fields_beamer
WOLF_DIR    = wolf_beamer
ABEL_DIR    = abel_beamer
COPSS_DIR   = copss_beamer

.PHONY: all cross beamer wolf abel copss clean distclean

all: cross beamer wolf abel copss

cross:
	$(MAKE) -C $(CROSS_DIR) pdf

beamer:
	$(MAKE) -C $(BEAMER_DIR) pdf

wolf:
	$(MAKE) -C $(WOLF_DIR) pdf

abel:
	$(MAKE) -C $(ABEL_DIR) pdf

copss:
	$(MAKE) -C $(COPSS_DIR) pdf

clean:
	$(MAKE) -C $(CROSS_DIR) clean
	$(MAKE) -C $(BEAMER_DIR) clean
	$(MAKE) -C $(WOLF_DIR) clean
	$(MAKE) -C $(ABEL_DIR) clean
	$(MAKE) -C $(COPSS_DIR) clean

distclean: clean
	$(MAKE) -C $(CROSS_DIR) distclean
	$(MAKE) -C $(BEAMER_DIR) distclean
	$(MAKE) -C $(WOLF_DIR) distclean
	$(MAKE) -C $(ABEL_DIR) distclean
	$(MAKE) -C $(COPSS_DIR) distclean
