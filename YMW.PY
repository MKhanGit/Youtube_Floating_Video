## Python 3.6 ##
# Author: Mohsin Khan
# Published: Sept. 18, 2018
# Notes: Enter a youtube video code or url, and this script will launch a
# Google Chrome Applet with just that video embedded in it.
# This is useful if you wish to have a minimal window just the youtube video in it

#NOTE: Change the settings below to set the location of Google Chrome
CHROME_APP = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

import sys, subprocess, os

HTMLFILE = 'YT.HTML'
PRJDIR = os.path.dirname(os.path.realpath(__file__)) + "\\"

try:
    VIDCODE = sys.argv[1]
    VIDCODE = str(VIDCODE)
except:
    VIDCODE = input('Enter Youtube video code or url: ')
    VIDCODE = str(VIDCODE)

if ".com" in VIDCODE:
    VIDCODE = VIDCODE.split('=')
    VIDCODE = VIDCODE[1]


YTFH = open(PRJDIR+HTMLFILE,'w')

headertext ='''
<!DOCTYPE-HTML>
<html>
<head>

</head>
<body>
'''

footertext ='''
</body>
</html>
'''

YTFH.write(headertext)
YTFH.write('\r\n')
YTFH.write('<iframe width="100%" height="100%" src="https://www.youtube.com/embed/')
YTFH.write(VIDCODE)
YTFH.write('?autoplay=1')
YTFH.write('" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>')
YTFH.write('\r\n')
YTFH.write(footertext)
YTFH.close()

subprocess.run([CHROME_APP, "-app="+PRJDIR+HTMLFILE])
