dir = $(pwd)
cd ~
[ ! -d .configbuilt ] && mkdir .configbuilt
cd .configbuilt
wget https://raw.githubusercontent.com/Ccode-lang/angledat/main/angledat.py
cp $dir/configbuilt.py .
