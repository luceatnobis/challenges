#!/usr/bin/env python

import Image
import sys 
import hashlib
import urllib
import urllib2
import cookielib

from cStringIO import StringIO
from operator import eq, itemgetter
from itertools import groupby

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

def unscramble(filename):

	column = 0
	rows = dict()
	try:
		image = Image.open(filename).convert('RGB')
	except IOError:
		print "Datei "+filename+" konnte nicht gefunden werden."
		sys.exit()
	image.save("exampleA.png")
	a = image.load()
	xDim, yDim = image.size
	oddOne = map(eq,a[0,0],a[0,1]).index(False)

	new = Image.new('RGB', (xDim, yDim))
	newLoad = new.load()

	for y in range(yDim):
		rows[a[0,y][oddOne]] = y
	
	for y in range(256):
		if y in rows:
			for x in range(xDim):
				newLoad[x, column] = a[x, rows[y]]
			column = column + 1
	return new

def readNotes(filename):
	try:
		notesHandle = open(filename)
	except IOError:
		print str(filename)+" konnte nicht gefunden werden."
		sys.exit()

	hashTable = dict()
	char, md5 = "", "" 

	for line in notesHandle:
		chomped = line.rstrip()
		index = chomped.find(':')
		char = chomped[:index]
		md5 = chomped[index+1:len(chomped)]
		hashTable[md5] = char

	return hashTable
	
def main():
	hashTable = readNotes('notes')
	browser = login()
	solution = ""

	resp = browser.open("http://www.enigmagroup.org/missions/programming/8/image.php")
	filePointer = StringIO(resp.read())
	img = unscramble(filePointer)
	img.save("exampleB.png")

	xDim, yDim = img.size
	cols = []
	loaded = img.load()

	for y in range(yDim):
		col = loaded[0, y]
		for x in range(xDim):
			if loaded [x,y] == col:
				loaded[x,y] = (0,0,0)
	
	for x in range(xDim):
		for y in range(yDim):
			if loaded[x, y] != (0,0,0) and x not in cols:
				cols.append(x)
	img.save("exampleC.png")	
	for k, g in groupby(enumerate(cols), lambda (i,x):i-x):
		columns =  map(itemgetter(1), g)
		md5 = hashlib.md5()
		hashString = ""
		for y in range(yDim):
			for x in columns:
				if loaded[x, y] != (0,0,0):
					#sys.stdout.write('#')
					hashString = hashString + '#'
				else:
					#sys.stdout.write(' ')
					hashString = hashString + ' '
			#sys.stdout.write('\n')
		md5.update(hashString)
		hashed = md5.hexdigest()
		#print hashed
		try:
			solution = solution + hashTable[hashed]
		except KeyError:
			print "Tut mir leid, ich bin ein dummes Programm :("
			sys.exit()
	
	solutionDict = urllib.urlencode({
		'answer' : solution,
		'submit' : 1
	})

	headers = {'Referer' : "http://www.enigmagroup.org/missions/programming/8/image.php"} 
	
	request = urllib2.Request("http://www.enigmagroup.org/missions/programming/8/image.php",
		solutionDict,
		headers
	)
	resp = browser.open(request)
	print resp.read()

main()
