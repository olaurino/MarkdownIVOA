
if not exist output\NUL mkdir output

pandoc -s -N --toc --template %~dp0..\ivoa-template.html^
  --filter %~dp0../filters/include.py --filter pandoc-crossref --filter pandoc-citeproc^
  --css %~dp0..\style\ivoa_doc.css --css %~dp0..\style\ivoa-plus.css^
  %*^
  -o output\full.html
