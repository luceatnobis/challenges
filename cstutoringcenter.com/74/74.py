#!/usr/bin/env python

from datetime import date

def main():
	for i in range(100):
            year = i % 365 if 365 < i else 0
            year += 1900

            date(2012,12,29).isoweekday()

main()
