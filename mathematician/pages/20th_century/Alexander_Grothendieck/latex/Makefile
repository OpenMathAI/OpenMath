# Auto-generated per-person Makefile.
NAME := Alexander_Grothendieck
TEX  := $(NAME).tex
PDF  := $(NAME).pdf

.PHONY: all pdf build clean distclean

# 默认目标：编译 + 清理中间产物，只保留 PDF
all: pdf

# 仅编译，不清理（保留 .aux/.log 等，方便调试）
build: $(PDF)

# 编译完成后调用 clean 清掉中间产物
pdf: $(PDF)
	@$(MAKE) --no-print-directory clean

$(PDF): $(TEX) body.tex metadata.tex ../../../../common/preamble.tex
	latexmk -xelatex -interaction=nonstopmode -halt-on-error $(TEX)

clean:
	@latexmk -c $(TEX) >/dev/null 2>&1 || true
	@rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz *.xdv

distclean: clean
	rm -f $(PDF)
