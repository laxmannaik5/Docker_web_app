#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type: text/html")
print()

f=cgi.FieldStorage()
cmd=f.getvalue("x")
#print(cmd)


#print("hi LW")

o=sp.getoutput("sudo "+cmd)
print(o)
