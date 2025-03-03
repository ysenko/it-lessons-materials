.PHONY: clean

clean:
	find . -name "*.html" -exec rm -f {} \;
	find . -name "*.pdf" -exec rm -f {} \;
	find . -name "*.pptx" -exec rm -f {} \;
