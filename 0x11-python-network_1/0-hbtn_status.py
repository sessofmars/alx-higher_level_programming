#!/usr/bin/python3
import urllib.request

req = urllib.request.Request('http://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
