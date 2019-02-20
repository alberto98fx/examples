#!/usr/bin/python3.6

"""MetaCall Examples - Auth Function Mesh.

[MetaCall](https://metacall.io)
[MetaCall Examples](https://github.com/metacall/examples)

This modules demonstrates a basic example of a python backend that executes
a call to another backend written in JavaScript (NodeJS).

""" 

from metacall import metacall_load_from_file, metacall

metacall_load_from_file('node', ['auth/auth.js'])

def login(text):
	return metacall('sign', text)

def time(token):
	return metacall('verify', token)