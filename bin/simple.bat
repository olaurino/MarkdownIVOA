
if not exist output\NUL mkdir output

pandoc -s -N --toc --template %~dp0..\ivoa-template.html --mathjax^
  --filter pandoc-citeproc^
  --css %~dp0..\style\ivoa_doc.css --css %~dp0..\style\ivoa-plus.css^
  %*^
  -o output\simple.html
