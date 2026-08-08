# Top-level Makefile for the Turing Award video series.
#
# Usage:
#   make                  build all episode PDFs
#   make pdf              same as above
#   make images           generate slide images for all episodes
#   make video            synthesize video for all episodes
#   make clean            remove intermediate files
#   make distclean        remove all generated files
#
#   make EP=00            build episode 00 only
#   make EP=01,03         build episodes 01 and 03

comma := ,

EPISODES := episode-00-what-is-turing-award \
            episode-01-theory-computation \
            episode-02-programming-languages \
            episode-03-ai-ml \
            episode-04-os-architecture \
            episode-05-database \
            episode-06-network-web \
            episode-07-distributed-verification \
            episode-08-crypto-security \
            episode-09-numerical-hpc \
            episode-10-graphics-hci \
            episode-allinone

ifdef EP
  _ep_nums := $(subst $(comma), ,$(EP))
  _ep_dirs  := $(foreach n,$(_ep_nums),$(filter episode-$n-%,$(EPISODES)))
  TARGETS   := $(_ep_dirs)
else
  TARGETS   := $(EPISODES)
endif

.PHONY: all pdf images video clean distclean list

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
