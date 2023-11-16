rm ./src/README.md
rm ./src/LICENSE.md
rm ./src/acknowledgements.md

find ./book/ -type f -name "*.html" -exec sed -i "s/README.html/index.html/g" {} +
sed -i "s/\/src\//\//g" ./book/index.html