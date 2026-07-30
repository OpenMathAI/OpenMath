# Top-level Makefile for Wolf Prize documentary series.
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
#   make EP=01,05         build episodes 01 and 05
#   make -j4 pdf          build all PDFs in parallel (4 jobs)

EPISODES := episode-01-origins-and-first-tradition \
            episode-02-bourbaki-homology-algebraic-geometry \
            episode-03-complex-harmonic-pde \
            episode-04-applied-free-boundary-wavelets \
            episode-05-probability-stochastic-geometry \
            episode-06-topology-revolution \
            episode-07-differential-geometric-analysis-symplectic \
            episode-08-number-theory-langlands \
            episode-09-hodge-representation-algebraic-geometry \
            episode-10-groups-combinatorics-computation \
            episode-11-dynamical-systems-ergodic-theory \
            episode-12-functional-analysis-logic \
            episode-allinone

# Determine which episodes to build.
# EP can be a comma-separated list like "01,05" (or "allinone").
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