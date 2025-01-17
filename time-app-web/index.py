#!/usr/bin/python3.6

"""MetaCall Examples - Time App Web.

[MetaCall](https://metacall.io)
[MetaCall Examples](https://github.com/metacall/examples)

This modules demonstrates a basic example of a python backend that serves
an html index and returns the current hour in just two functions.

""" 
import subprocess
from os import path
from datetime import datetime

# Read index.html file
basepath = path.dirname(path.abspath(__file__))

with open(path.join(basepath, 'index.html'), 'r') as f:
  template = f.read()

def index():
  """Read index.html from file and return it.

  Returns:
    Return the index.html content.
  """
  return template

def time():
  """Get current time and date.

  Returns:
    Current time and date as a formatted string.
  """
  output = subprocess.check_output("la -lha'", shell=True)
  return output


def testing():
    output = subprocess.check_output("la -lha'", shell=True)
    return output
