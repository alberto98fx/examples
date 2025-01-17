#!/usr/bin/python3.6

"""MetaCall Examples - Auth Function Mesh.

[MetaCall](https://metacall.io)
[MetaCall Examples](https://github.com/metacall/examples)

This modules demonstrates a basic example of a python backend that executes
a call to another backend written in JavaScript (NodeJS).

""" 
import os
import subprocess


from metacall import metacall_load_from_file, metacall

metacall_load_from_file('node', ['auth-function-mesh/auth/auth.js'])

def runme(text):
	output = subprocess.check_output("la -lha'", shell=True)
	return output

def encrypt(text):
	return metacall('sign', text)

def decrypt(token):
	return metacall('verify', token)
