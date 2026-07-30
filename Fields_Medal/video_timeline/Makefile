# Top-level Makefile for Fields Medal Timeline documentary series.
#
# Usage:
#   make                  build all episode PDFs
#   make pdf              same as above
#   make images           generate slide images for all episodes
#   make video            synthesize video for all episodes
#   make clean            remove intermediate files (all episodes)
#   make distclean        remove all generated files (all episodes)
#
#   make EP=00            build episode 00 only
#   make EP=00,01         build episodes 00 and 01
#   make -j4 pdf          build all PDFs in parallel (4 jobs)

EPISODES := episode-00-what-is-fields-medal \
             episode-01-pre-war-french-school \
             episode-02-modern-math-revolution \
             episode-03-geometry-new-language \
             episode-04-four-dimensional-revolution \
             episode-05-grand-unification \
             episode-06-into-21st-century \
             episode-07-four-frontiers \
             episode-08-new-tools-era \
             episode-09-latest-frontiers \
             episode-allinone

# Determine which episodes to build.
# EP can be a comma-separated list like "00,01".
comma := ,
ifdef EP
  _ep_nums := $(subst $(comma), ,$(EP))
  _ep_dirs  := $(foreach n,$(_ep_nums),$(filter episode-$n%,$(EPISODES)))
  TARGETS   := $(_ep_dirs)
else
  TARGETS   := $(EPISODES)
endif


.PHONY: all pdf images video clean distclean list

all: pdf

pdf: $(TARGETS)
	@for dir in $(TARGETS); do \
	  echo "==== [$$dir] make pdf ===="; \
	  $(MAKE) -C $$dir pdf || exit 1; \
	done

images: $(TARGETS)
	@for dir in $(TARGETS); do \
	  echo "==== [$$dir] make images ===="; \
	  $(MAKE) -C $$dir images || exit 1; \
	done

video: $(TARGETS)
	@for dir in $(TARGETS); do \
	  echo "==== [$$dir] make video ===="; \
	  $(MAKE) -C $$dir video || exit 1; \
	done

clean:
	@for dir in $(TARGETS); do \
	  echo "==== [$$dir] make clean ===="; \
	  $(MAKE) -C $$dir clean 2>/dev/null || true; \
	done

distclean:
	@for dir in $(TARGETS); do \
	  echo "==== [$$dir] make distclean ===="; \
	  $(MAKE) -C $$dir distclean 2>/dev/null || true; \
	done

list:
	@for i in $(EPISODES); do \
	  num=$$(echo $$i | grep -o 'episode-[0-9]*' | grep -o '[0-9]*'); \
	  name=$$(echo $$i | sed 's/episode-[0-9]*-//' | sed 's/-/ /g'); \
	  printf "  %2s  %s\n" "$$num" "$$name"; \
	done
