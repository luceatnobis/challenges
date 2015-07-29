#!/usr/bin/env python

import sys
import os
import urllib2
import urllib
import cookielib
import Image
import hashlib

from operator import itemgetter 
from itertools import groupby
from cStringIO import StringIO

def login():
	userData = urllib.urlencode({
		'user' : sys.argv[1],
		'passwrd' : sys.argv[2],
		'cookielength' : -1
	})

	cookies = cookielib.CookieJar()

	opener = urllib2.build_opener(
		urllib2.HTTPHandler(debuglevel=0),
		urllib2.HTTPCookieProcessor(cookies)

	)
	headers = {'Referer' : 'http://penisse.de'}
	wat = urllib2.Request(
		"http://www.enigmagroup.org/forums/index.php?action=login2",
		userData,
		headers
	)
	opener.open("http://www.enigmagroup.org/forums/index.php?action=login2",data = userData)
	return opener

def readNotes(filename):
	return None
	try:
		a = open(filename,"r")
	except IOError:
		print filename+" konnte nicht gefunden werden."
	
	hashes = dict()
	for line in a:
		split = line.rstrip().split(':')
		hashes[split[1]] = split[0]

	return hashes

def crack(filename, hashTable):

	done = False
	solution = ""
	upperLimit, lowerLimit = 0, 0

	try:
		image = Image.open(filename).convert('RGB')
	except IOError:
		print "Datei "+filename+" konnte nicht gefunden werden."
		sys.exit()

	image.show()
	sys.exit()
	xDim, yDim = image.size
	
	ram = image.load()
	cols = []

	""" Wir bemuehen uns, das obere Limit fuer schwarz rauszukriegen """
	for y in range(yDim):
		for x in range(xDim):
			if ram[x, y] != (255,255,255):
				upperLimit = y
				done = True
				break
		
		if done:
			break
	
	""" Wieder zuruecksetzen das ganze """
	done = False 

	""" Nun das gleiche fuer das untere Limit """
	for y in range(yDim)[::-1]:
		for x in range(xDim):
			if ram[x, y] != (255,255,255):
				lowerLimit = y
				done = True
				break
		if done:
			break
	""" Wir speichern, in welchen Spalten schwarz ist """
	for x in range(xDim):
		for y in range(upperLimit, 39):
			if ram[x, y] != (255, 255, 255):
				cols.append(x)
				break

	""" Wir lassen uns alle Spalten ausgeben welche aufeinander folgen """	
	for k, g in groupby(enumerate(cols), lambda (i,x):i-x):
		columns = map(itemgetter(1), g) #Hier sind wir an einem neuen Buchstaben angekommen. 
		charString , charHash = "", ""
		for y in range(upperLimit, lowerLimit+1):
			for x in columns:
				if ram[x, y] == (255,255,255):
					charString += (' ')
				else:
					charString += ('#')
			charString += ('\n')
		#print charString
		charHash = hashlib.md5(charString).hexdigest()
		#print charHash
		try:
			solution += hashTable[charHash]
		except KeyError:
			print "Ich bin ein dummes Programm."
			print charString
			print charHash
			sys.exit()
	image.show()
	return solution

def clean(filepointer):
	colours = {}
	image = Image.open("analysis.png")
	ram = image.load()
	xDim, yDim = image.size
	image.show()
	his = image.histogram()
	print len(his)
	sys.exit()
def main():
	"""
	browser = login()
	resp = browser.open("http://www.enigmagroup.org/missions/captcha/2/image.php")
	filePointer = StringIO(resp.read())
	"""
	clean("wat")
	"""
	hashTable = readNotes("notes")
	solution = crack(filePointer, hashTable)
	sys.exit()
	solutionDict = urllib.urlencode({
		'answer' : solution,
		'submit' : 1
	})

	headers = {'Referer' : "http://www.enigmagroup.org/missions/captcha/1/image.php"}

	request = urllib2.Request("http://www.enigmagroup.org/missions/captcha/1/image.php",
		solutionDict,
		headers
	)
	resp = browser.open(request)
	print resp.read()
	"""
main()
