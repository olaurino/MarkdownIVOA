pandoc -s -N --toc --template %~dp0..\ivoa-simple.html^
  --filter pandoc-citeproc^
  --css %~dp0..\style\ivoa_doc.css --css %~dp0..\style\ivoa-plus.css^
  %*^
  -o %~dp0..\output\simple.html
