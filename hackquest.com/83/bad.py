#!/usr/bin/env python

import Image
import requests
from cStringIO import StringIO
from colorama import Fore
import hashlib
import sys
import mechanize

wat = {
	"VIRUS!" : "Hello+I+am+a+virus%2C+and+I+come+from+HackQuest%21+Boooh%21+Be+scared%21",
	"Force" : "TG9vaywgYSBwYXNzd29yZCFVM0JsYkd4R2IzSmpaUT09",
	"POSTNUKESID" : "c5659f9645d62a6184a35c8ab03de832",
	"phpbb2mysql_data" : "a%3A1%3A%7Bs%3A6%3A%22userid%22%3Bs%3A6%3A%22165947%22%3B%7D",
	"phpbb2mysql_sid" : "99133d3258c07fa1d9394cc43f65954f",
	"ChallUID" : "165947",
	"ChallUNAME" : "username"
}

#def request():
mech = mechanize.Browser()
mech.set_handle_robots(False)
mech.open("http://hackquest.com")
mech.select_form(nr=0)
mech["uname"] = sys.argv[1]
mech["pass"] = sys.argv[2]
mech.submit()
resp = mech.open("http://hackquest.com/modules.php?op=modload&name=HackQuest&file=challengestart&cid=74")
resp = mech.open("http://hackquest.com/modules/HackQuest/hacking/9841263762/9841263762.php")
resp = mech.open("http://hackquest.com/modules/HackQuest/hacking/9841263762/service.php")
print resp.read()
sys.exit()
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

def readBig(filename):
	xWidth = 19
	hashes = readNotes("notes")

	solutionString = ""

	try:
		img = Image.open(filename).convert("RGB")
	except IOError:
		print "Die angegebende Datei existiert nicht."
		sys.exit()
	
	ram = img.load()

	xDim, yDim = img.size
	
	for fac in range(4):
		hashString = ""
		xStart = 5 + fac * 25
		xEnd = xStart + 25

		for y in range(5,30):
			for x in range(xStart,xEnd):
				if ram[x,y] == (0,255,0):
					hashString += " "
				else:
					hashString += "#"
					ram[x,y] = (0,0,0)
		hashString = hashlib.md5(hashString).hexdigest()
		try:
			solutionString += hashes[hashString]
		except KeyError:
			print "Da lief wohl was schief"
	return solutionString.lower()

def readSmall(filepointer):
	hashes = readNotes("notes")
	
	try:
		img = Image.open(filepointer).convert("RGB")
	except IOError:
		print "Die angegebende Datei existiert nicht."
		sys.exit()

	solutionString = ""
	ram = img.load()

	for y in (36,51):
		binary = ""
		
		for x in range(6,102)[::5]:
			binary += "0" if sum(ram[x,y]) > 0 else "1"
		
		for i in range(len(binary))[::4]:
			for char in binary[i:i+4]:
				if char == "0":
					sys.stdout.write(Fore.RED+ char + Fore.WHITE)
				else:
					sys.stdout.write(Fore.BLACK + char + Fore.WHITE)
			print
		#print hashlib.md5(binary).hexdigest()
		print 
		pianoHash = hashlib.md5(binary).hexdigest()
		solutionString += hashes[pianoHash]		

	return solutionString
def main():
	request()
	"""
	browser = request()
	solutionString = ""

	filePointer = StringIO(browser.content)
	solutionString += readBig(filePointer)
	
	filePointer = StringIO(browser.content)
	solutionString += readSmall(filePointer)

	print solutionString
	post = {'solution' : solutionString}#, 'submit' : 'Enter'}
	ans = requests.post(
		"http://hackquest.com/modules/HackQuest/hacking/9841263762/9841263762.php",
		cookies=wat,
		data=post,
		headers={'Referer' : "http://hackquest.com/modules/HackQuest/hacking/9841263762/9841263762.php"}
	)
	print ans.content
	"""
main()
