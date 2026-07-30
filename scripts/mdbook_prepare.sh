cp ./README.md ./src/
# "-i.bak" is portable across GNU sed (Linux/CI) and BSD sed (macOS); a bare
# "-i" consumes the next argument as the backup suffix on BSD.
LC_ALL=C sed -i.bak -e 's/src\/img/img/g' ./src/README.md
rm -f ./src/README.md.bak

cp ./LICENSE.md ./src/
cp ./acknowledgements.md ./src/