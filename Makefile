.PHONY: clean

SRC ?= presentation.md
OUTPUT_DIR ?= output

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
	rm -rf $(OUTPUT_DIR)


# Show help message
help:
	@echo "Usage: make [target] [SRC=path/to/yourfile.md]"
	@echo "Available targets:"
	@echo "  html     - Generate HTML presentation (default: presentation.md)"
	@echo "  clean    - Remove ALL pdf, html and pptx files"
	@echo "  help     - Show this help message"
	@echo "Example usage: make html SRC=my_presentation.md"
