#!/bin/sh

mkdir -p /usr/share/gtweetbar
cp -R ./python_twitter /usr/share/gtweetbar/
cp README /usr/share/gtweetbar/

cp gtweetbar.py /usr/local/bin/
chmod u+x /usr/local/bin/gtweetbar.py
chmod g+x /usr/local/bin/gtweetbar.py
chmod a+x /usr/local/bin/gtweetbar.py
cp gtweetbar.server /usr/lib/bonobo/servers/

echo "Done!"

