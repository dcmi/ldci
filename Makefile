D2695955.md: D2695955.json
	python3 mkci.py

D2695955.html: D2695955.md
	pandoc -f markdown_github -t html -o D2695955.html D2695955.md

D2695955.pdf: D2695955.html
	wkhtmltopdf D2695955.html D2695955.pdf
