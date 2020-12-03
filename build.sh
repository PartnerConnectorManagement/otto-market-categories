rm -r public
mkdir public
mkdir public/images
mkdir public/jsons
mkdir jsons
python3 download.py

cp *.html public/
cp *.css public/
cp *.js public/
cp -a images/. public/images
cp -a jsons/. public/jsons