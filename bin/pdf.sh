#!/bin/bash -xe

bindir=$( cd -P "$( dirname "$0" )" && pwd )
if [ -h "$0" ]; then
  bindir=$( cd -P "$( dirname "`readlink -n "$0"`" )" && pwd )
fi

mkdir -p output

pandoc -s -N --toc --template $bindir/../ivoa-template.tex\
  --latex-engine=xelatex --listings\
  --filter $bindir/../filters/include.py --filter pandoc-crossref --filter pandoc-citeproc\
  --css $bindir/../style/ivoa_doc.css --css $bindir/../style/ivoa-plus.css\
  $*\
  -o output/full.pdf
