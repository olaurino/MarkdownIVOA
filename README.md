To compile the test document:

````
pandoc --template ivoa-template.tex --filter pandoc-citeproc metadata.yaml test.md -o test.pdf
````
