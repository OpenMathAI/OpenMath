# Top-level Makefile for Fields Medal video episodes.
#
# Usage:
#   make                  build all episode PDFs
#   make pdf              same as above
#   make images           generate slide images for all episodes
#   make video            synthesize video for all episodes
#   make clean            remove intermediate files (all episodes)
#   make distclean        remove all generated files (all episodes)
#
#   make EP=01            build episode 01 only
#   make EP=01,05,13      build episodes 01, 05, 13
#   make pdf EP=03        build PDF for episode 03 only
#   make -j4 pdf          build all PDFs in parallel (4 jobs)

EPISODES := episode-01-complex-harmonic-extremal \
            episode-02-pde-applied-analysis \
            episode-03-differential-geometry-geometric-analysis \
            episode-04-differential-topology-manifold-theory \
            episode-05-modern-geometry-revolution \
            episode-06-algebraic-geometry-foundations \
            episode-07-algebraic-geometry-mordell-minimal-models \
            episode-08-number-theory-classical \
            episode-09-number-theory-langlands-arithmetic-geometry \
            episode-10-foundations-algebraic-structures \
            episode-11-dynamical-systems-chaos-ergodic-theory \
            episode-12-modern-probability-random-analysis-stat-physics \
            episode-13-rise-of-combinatorics

# Determine which episodes to build.
# EP can be a comma-separated list like "01,02,05".
ifdef EP
  _ep_nums := $(subst $(comma), ,$(EP))
  _ep_dirs  := $(foreach n,$(_ep_nums),$(filter episode-$n-%,$(EPISODES)))
  TARGETS   := $(_ep_dirs)
else
  TARGETS   := $(EPISODES)
endif

comma := ,

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
