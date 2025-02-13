#!/bin/bash
set +ex

VERSION="6.3.1"
URL="https://github.com/olifolkerd/tabulator/archive/refs/tags/$VERSION.zip"
OUTPUT_ZIP="dist.zip"
curl -L -o $OUTPUT_ZIP $URL
#unzip $OUTPUT_ZIP
#rm $OUTPUT_ZIP
#
#rm -dr js_lib_tabulator/static/tabulator
#mv dist js_lib_tabulator/static/tabulator
