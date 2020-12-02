rm -r public
mkdir public
mkdir public/images
python3 download.py

cp index.html public/index.html
cp style.css public/style.css
cp index.js public/index.js
cp images/logo.png public/images/logo.png