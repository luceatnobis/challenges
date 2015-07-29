#!/usr/bin/env python

from hashlib import md5
import requests
import re

def main():
	
	url = "https://hax.tor.hu/level11/"
	cookies = { "HAXTOR" : "3670111a993987f7faccc3a1f17557b4"}	
	hashObj = md5()

	site = requests.get(url, cookies = cookies,verify = False).text
	string = "".join(re.findall("Enter the hash for: \"<b>(.+?)</b>", site)[0].replace(" ",""))
	
	hashObj.update(string)
	md5String = hashObj.hexdigest()
	
	params = { 'pw' : md5String }
	#text = requests.get(url, params = params, verify = False).text
	text = requests.get("https://hax.tor.hu/level11/?pw="+md5String, verify = False, cookies = cookies).text
	print text

main()
