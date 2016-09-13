
if not exist output\NUL mkdir output

pandoc -s -N --toc --template %~dp0..\ivoa-template.html --mathjax^
  --filter %~dp0../filters/include.py --filter pandoc-crossref --filter pandoc-citeproc^
  --css ..\cereal\style\ivoa_doc.css --css ..\cereal\style\ivoa-plus.css^
  %*^
  -o output\full.html
