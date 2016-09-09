#!/bin/bash -x

pandoc -s -N --toc --template ivoa-simple.html\
  --filter pandoc-citeproc\
  --css ../style/ivoa_doc.css --css ../style/ivoa-plus.css\
  $*\
  -o output/simple.html
