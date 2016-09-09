#!/bin/bash -xe

pandoc -s -N --toc --template ivoa-template.html\
  --filter filters/include.py --filter pandoc-citeproc\
  --css ../style/ivoa_doc.css --css ../style/ivoa-plus.css\
  $*\
  -o output/full.html
