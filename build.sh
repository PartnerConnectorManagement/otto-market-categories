rm -r public
mkdir public
mkdir public/images
mkdir public/jsons
python3 download.py

cp index.html public/index.html
cp style.css public/style.css
cp index.js public/index.js
cp -a images/. public/images
cp -a jsons/. public/jsons