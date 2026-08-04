# =============================================================
#  OpenMath 数学家立传 —— 顶层 Makefile
#
#  自动发现所有含 Makefile 的子目录，递归调用子 Make。
#  新增数学家只需在对应目录下放好 Makefile，无需修改本文件。
#
#  Usage:
#    make             构建全部 PDF
#    make Alan_Turing  只构建 Alan_Turing
#    make clean        清理全部中间文件
#    make distclean    清理全部中间文件 + PDF
#    make -j4          4 路并行构建
# =============================================================

# 自动发现所有含 Makefile 的子目录（排除无 Makefile 的目录如 prompts）
SUBDIRS := $(patsubst %/Makefile,%,$(wildcard */Makefile))

.PHONY: all pdf clean distclean $(SUBDIRS)

all: pdf

pdf: $(SUBDIRS)

# 每个子目录作为一个伪目标，递归调用其 Makefile
$(SUBDIRS):
	$(MAKE) -C $@

clean:
	@for d in $(SUBDIRS); do \
		echo "=== cleaning $$d ==="; \
		$(MAKE) -C $$d clean 2>/dev/null || true; \
	done

distclean:
	@for d in $(SUBDIRS); do \
		echo "=== distclean $$d ==="; \
		$(MAKE) -C $$d distclean 2>/dev/null || true; \
	done

# 列出已发现的子目录
list:
	@echo "Discovered subdirectories ($(words $(SUBDIRS))):"
	@for d in $(SUBDIRS); do echo "  $$d"; done
