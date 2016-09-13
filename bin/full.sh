#!/bin/bash -xe

bindir=$( cd -P "$( dirname "$0" )" && pwd )
if [ -h "$0" ]; then
  bindir=$( cd -P "$( dirname "`readlink -n "$0"`" )" && pwd )
fi

mkdir -p output

pandoc -s -N --toc --template $bindir/../ivoa-template.html --mathjax\
  --filter $bindir/../filters/include.py --filter pandoc-crossref --filter pandoc-citeproc\
  --css ../cereal/style/ivoa_doc.css --css ../cereal/style/ivoa-plus.css\
  $*\
  -o output/full.html
