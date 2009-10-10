#!/bin/sh

echo 'GTweetBar 1.0 Installer'
echo ' *** you must be a super user to be able to install *** '
echo ' '
echo 'Creating /usr/share/gtweetbar'
mkdir -p /usr/share/gtweetbar

echo 'Copying needed resource files'
cp -R ./python_twitter /usr/share/gtweetbar/
cp -R ./ui /usr/share/gtweetbar/
cp README /usr/share/gtweetbar/

echo 'Copying main script into /usr/local/bin'
cp gtweetbar.py /usr/local/bin/

echo 'Setting up permissions'
chmod u+x /usr/local/bin/gtweetbar.py
chmod g+x /usr/local/bin/gtweetbar.py
chmod a+x /usr/local/bin/gtweetbar.py
cp gtweetbar.server /usr/lib/bonobo/servers/

echo "Done!"
echo "Do a right click on desired panel, and add Gnome TweetBar to it"

