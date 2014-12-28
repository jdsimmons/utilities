#! /usr/bin/env python
from BeautifulSoup import  BeautifulSoup

soup = BeautifulSoup(open("youtube.html"))

i = 0
previous_url = ''

for link in soup.findAll('a'):
    url = link.get('href')
    text = unicode(link.string)
    if text != 'None' and 'watch?v=' in url:
        print('# ' + text)
    if 'watch?v=' in url  and  url != previous_url:
        i = i + 1
        trimmed_url = url[:20]
        print('youtube-dl https://www.youtube.com' +  trimmed_url), 
        previous_url = url
print 'Total links is: ',  i
