#!/bin/bash -xe

bindir=$( cd -P "$( dirname "$0" )" && pwd )
if [ -h "$0" ]; then
  bindir=$( cd -P "$( dirname "`readlink -n "$0"`" )" && pwd )
fi

mkdir -p output

pandoc -s -N --toc --template $bindir/../ivoa-template.html --mathjax\
  --filter pandoc-citeproc\
  --css ../cereal/style/ivoa_doc.css --css ../cereal/style/ivoa-plus.css\
  $*\
  -o output/simple.html

yes | cp -rfT media output/media || echo "warning: can't copy media folder" 
