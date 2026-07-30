# Top-level Makefile for the Abel Prize video series.
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
#   make EP=01,02         build episodes 01 and 02
#   make -j4 pdf          build all PDFs in parallel (4 jobs)

comma := ,

EPISODES := episode-00-what-is-abel-prize \
             episode-01-foundations-2003-2007 \
             episode-02-algebra-geometry-2008-2013 \
             episode-03-analysis-numbers-2014-2019 \
             episode-04-new-frontiers-2020-2026 \
             episode-allinone

ifdef EP
  _ep_nums := $(subst $(comma), ,$(EP))
  _ep_dirs  := $(foreach n,$(_ep_nums),$(filter episode-$n-%,$(EPISODES)))
  TARGETS   := $(_ep_dirs)
else
  TARGETS   := $(EPISODES)
endif

.PHONY: all pdf images video clean distclean list $(EPISODES)

all: pdf

pdf:
	@for d in $(TARGETS); do echo "==> $$d (pdf)"; $(MAKE) -C $$d pdf || exit $$?; done

images:
	@for d in $(TARGETS); do echo "==> $$d (images)"; $(MAKE) -C $$d images || exit $$?; done

video:
	@for d in $(TARGETS); do echo "==> $$d (video)"; $(MAKE) -C $$d video || exit $$?; done

clean:
	@for d in $(EPISODES); do $(MAKE) -C $$d clean; done

distclean:
	@for d in $(EPISODES); do $(MAKE) -C $$d distclean; done

list:
	@echo "Episodes:"; for d in $(EPISODES); do echo "  $$d"; done
