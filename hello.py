#!/usr/bin/env python3
import cgi, cgitb
cgitb.enable()
import os 

print("Content-Type: text/html\n")
print()
print("<!doctype html><title>Hello</title><h2>Hello World</h2>")

#question1
print(os.environ)

#quesiton2
#print(os.environ["QUERY_STRING"])

#question3
#print(os.environ["HTTP_USER_AGENT"])