#!/bin/bash -xe

bindir=$( cd -P "$( dirname "$0" )" && pwd )
if [ -h "$0" ]; then
  bindir=$( cd -P "$( dirname "`readlink -n "$0"`" )" && pwd )
fi

mkdir -p output

pandoc -s -N --toc --template $bindir/../ivoa-template.html --mathjax\
  --filter pandoc-citeproc\
  --css $bindir/../style/ivoa_doc.css --css $bindir/../style/ivoa-plus.css\
  $*\
  -o output/simple.html
