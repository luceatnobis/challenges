#!/usr/bin/env python

class bacteria():
	def __init__(self):
		self.total = 0
		self.state = [1,0,0,0,0]
		self.temp = [0,0,0,0,0]
	
	def day1(self):
		self.temp[0] += self.state[0]
		self.state[0] = 0
	
	def day2(self):
		for i in range(self.state[1]):
			self.temp[1] += 1
			self.state[1] = 0	

	def day3(self):
		for i in range(self.state[2]):
			self.temp[2] += 1
			self.state[2] = 0
	
	def day4(self):
		self.temp[3] += self.state[3]
		self.state[3] = 0
	
	def day5(self):
		self.state[4] = 0

	def day(self):
		self.day1()
		self.day2()
		self.day3()
		self.day4()
		self.day5()
		for i in range(len(self.state)):
			self.state[i] += self.temp[i]

def main():
	bac = bacteria()
	for i in range(8):
		print bac.state
		print bac.temp
		bac.day()
	print sum(bac.state)
main()
