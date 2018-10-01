# Not much here, this is a small package anyway
__all__ = ["pyana"]
__version__ = '0.4.1'


import sys
import os
import unittest
from . import _pyana

## Functions for loading in ANA files
def fzread(filename, debug=0):
	"""
	Load an ANA file and return the data, size, dimensions and comments in a
	dict.
	
	data = pyana.load(filename)
	"""
	if not os.path.isfile(filename):
		raise IOError("File does not exist!")
	
	data = _pyana.fzread(filename, debug)
	return data


def getdata(filename, debug=0):
	"""
	Load an ANA file and only return the data as a numpy array.
	
	data = pyana.getdata(filename)
	"""
	return (fzread(filename, debug))['data']
	# data = _pyana.fzread(filename, debug)
	# return data['data']

	
def getheader(filename, debug=0):
	"""
	Load an ANA file and only return the header consisting of the dimensions,
	size (defined as the product of all dimensions times the size of the
	datatype, this not relying on actual filesize) and comments.
	
	header = pyana.getheader(filename)
	"""
	return (fzread(filename, debug))['header']
	# data = _pyana.fzread(filename, debug)
	# return data['header']

## Functions for storing ANA files
def fzwrite(filename, data, compress=1, comments=False, debug=0):
	"""
	Save a 2d numpy array as an ANA file and return the bytes written, or NULL
	
	written = pyana.fzwrite(filename, data, compress=1, comments=False)
	"""
	if (comments):
		return _pyana.fzwrite(filename, data, compress, comments, debug)
	else:
		return _pyana.fzwrite(filename, data, compress, '', debug)


def writeto(filename, data, compress=1, comments=False, debug=0):
	"""
	Similar as pyana.fzwrite().
	"""
	return fzwrite(filename, data, compress, comments, debug)	
