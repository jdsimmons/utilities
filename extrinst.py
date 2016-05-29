#! /usr/bin/env python
from BeautifulSoup import  BeautifulSoup
from gi.repository import Gtk, Gdk

clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
text = clipboard.wait_for_text()
if text != None:
    soup = BeautifulSoup(text)
else:
    print("No text on the clipboard.")

# soup = BeautifulSoup(open("instagram.html"))

for link in soup.findAll('div'):
    url = link.get('src')
    if url is not None and '_n.' in url:
        print('wget ' +  url) 
