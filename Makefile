.PHONY: clean html-local

SRC ?= presentation.md
# Use content to ensure that produced html files can find images.
OUTPUT_DIR ?= content

# Output HTML file (derived from SRC name)
HTML_OUT = $(patsubst %.md,%.html,$(SRC))
PDF_OUT = $(patsubst %.md,%.pdf,$(SRC))
PPTX_OUT = $(patsubst %.md,%.pptx,$(SRC))

HTML_OUT := $(subst content,$(OUTPUT_DIR),$(HTML_OUT))
PDF_OUT := $(subst content,$(OUTPUT_DIR),$(PDF_OUT))
PPTX_OUT := $(subst content,$(OUTPUT_DIR),$(PPTX_OUT))

# Define Marp CLI command
MARP = marp

# Default target: generate HTML, PDF and PPTX files
all: html pdf pptx

# Generate HTML version of the presentation
html:
	$(MARP) $(SRC) --output $(HTML_OUT) --html --allow-local-files

# Generate all HTML presentations and rebuild index.html locally, then serve
html-local:
	$(MARP) content --html --allow-local-files
	PUBLISH_DIR=content python3 build_index_page.py
	@echo "Serving content at http://localhost:8000 — press Ctrl+C to stop"
	cd content && python3 -m http.server 8000

# Generate PDF version of the presentation
pdf:
	$(MARP) $(SRC) --output $(PDF_OUT) --pdf --allow-local-files

# Generate PPTX version of the presentation
pptx:
	$(MARP) $(SRC) --output $(PPTX_OUT) --pptx --allow-local-files

# Remove all PDF, HTML and PPTX files
clean:
	find . -name "*.html" -exec rm -f {} \;
	find . -name "*.pdf" -exec rm -f {} \;
	find . -name "*.pptx" -exec rm -f {} \;

# Show help message
help:
	@echo "Usage: make [target] [SRC=path/to/yourfile.md]"
	@echo "Available targets:"
	@echo "  html     - Generate HTML presentation (default: presentation.md)"
	@echo "  html-local - Generate HTML for all files in content and rebuild content/index.html"
	@echo "  clean    - Remove ALL pdf, html and pptx files"
	@echo "  help     - Show this help message"
	@echo "Example usage: make html SRC=my_presentation.md"
