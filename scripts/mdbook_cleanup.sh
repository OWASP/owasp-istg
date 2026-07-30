rm ./src/README.md
rm ./src/LICENSE.md
rm ./src/acknowledgements.md

# "-i.bak" is portable across GNU sed (Linux/CI) and BSD sed (macOS); a bare
# "-i" consumes the next argument as the backup suffix on BSD. LC_ALL=C stops
# BSD sed rejecting the generated HTML as an "illegal byte sequence".
find ./book/ -type f -name "*.html" ! -name "._*" -exec env LC_ALL=C sed -i.bak "s/README.html/index.html/g" {} +
LC_ALL=C sed -i.bak "s/\/src\//\//g" ./book/index.html
find ./book/ -type f -name "*.bak" ! -name "._*" -delete