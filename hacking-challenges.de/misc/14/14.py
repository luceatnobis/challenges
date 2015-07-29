#!/usr/bin/env python

from threading import Timer
import time
import requests

def main():
	waiting_in_secs = (60 * 60 * 5)
	cookies = {"PHPSESSID" : "edmqn3k25spovdc5u36cojtpdbs1sorm", "Hacking-Challenges" : "NDh8NGU4MmU2NjNlNTAwMmQ2MDZhZjY0NGYyOTViNjg2NWM%3D"}

	login_adress = "http://www.hacking-challenges.de/index.php?page=forum&view=login"
	resp = requests.get("http://www.hacking-challenges.de/", cookies=cookies)
	
	print "Started at " + time.strftime('%X %x %Z')
	print "Will wait for " + str(waiting_in_secs) + " seconds"
	timer = Timer(waiting_in_secs , get_page, [cookies])
	timer.start()

def get_page(cookies):
	print time.strftime('%X %x %Z')
	resp = requests.get("http://www.hacking-challenges.de/index.php?page=hackits&kategorie=misc&id=14", cookies=cookies)
	
	with open("solution", "w") as f:
		f.write(resp.content)

main()
