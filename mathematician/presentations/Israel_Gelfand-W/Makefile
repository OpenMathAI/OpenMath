# Makefile for Israel Gelfand beamer deck.
#
# Usage:
#   make            build the PDF
#   make pdf        same as above
#   make images     generate slide PNGs from the PDF
#   make video      synthesize an MP4 from slide images (+ optional BGM)
#   make clean      remove intermediate files
#   make distclean  remove generated PDF/images/video

MAIN        = Israel_Gelfand_zh
VIDEO_NAME  = Israel_Gelfand_zh
OUTPUT_DIR  = output
IMAGES_DIR  = $(OUTPUT_DIR)/images
SLIDES_TXT  = $(OUTPUT_DIR)/slides.txt

DURATION    = 7
# Optional background music: drop a .wav here and set BGM to its name.
BGM         = $(wildcard *.wav)

LATEXMK     = latexmk
PDFTOPPM    = pdftoppm
FFMPEG      = ffmpeg
PYTHON      = python3

.PHONY: all pdf images video clean distclean

all: pdf

pdf: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	-$(LATEXMK) -xelatex -synctex=0 -interaction=nonstopmode -f $(MAIN).tex
	-$(LATEXMK) -c $(MAIN).tex
	rm -f $(MAIN).{nav,snm,xdv}
images: $(IMAGES_DIR)/.done
$(IMAGES_DIR)/.done: $(MAIN).pdf
	@mkdir -p $(IMAGES_DIR)
	$(PDFTOPPM) -png -r 600 $(MAIN).pdf $(IMAGES_DIR)/slide
	@cd $(IMAGES_DIR) && for f in slide-*.png; do mv "$$f" "$$(echo $$f | sed 's/-/_/')"; done 2>/dev/null || true
	@touch $@
$(SLIDES_TXT): $(IMAGES_DIR)/.done
	@$(PYTHON) -c "import os; imgs=sorted([f for f in os.listdir('$(IMAGES_DIR)') if f.endswith('.png')]); lines=[]; [lines.extend(['file \"images/'+f+'\"','duration $(DURATION)']) for f in imgs]; lines.append('file \"images/'+imgs[-1]+'\"'); open('$(SLIDES_TXT)','w').write('\n'.join(lines)+'\n')"
video: $(OUTPUT_DIR)/$(VIDEO_NAME).mp4
$(OUTPUT_DIR)/$(VIDEO_NAME).mp4: $(SLIDES_TXT)
	@mkdir -p $(OUTPUT_DIR)
	$(FFMPEG) -y -f concat -safe 0 -i $(SLIDES_TXT) -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 15 -preset medium -r 24 $(OUTPUT_DIR)/$(VIDEO_NAME).tmp.mp4
	@mv $(OUTPUT_DIR)/$(VIDEO_NAME).tmp.mp4 $(OUTPUT_DIR)/$(VIDEO_NAME).mp4
clean:
	$(LATEXMK) -c $(MAIN).tex 2>/dev/null || true
	rm -f $(MAIN).{aux,log,toc,out,nav,snm,fls,fdb_latexmk,xdv} $(SLIDES_TXT) $(IMAGES_DIR)/.done c.log
distclean: clean
	rm -f $(MAIN).pdf
	rm -rf $(IMAGES_DIR) $(OUTPUT_DIR)/$(VIDEO_NAME).mp4
