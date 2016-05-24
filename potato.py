#!/usr/bin/python3

import potato.load
import potato.parse
import urllib.error
import time

def test():
	x = 0
	while (x < 10):
		item_list_json = potato.load.item_list(x, 100)
		item_list = potato.parse.item_list(item_list_json)
		i = 0
		while (i < len(item_list)):
			item = item_list[i]
			try:
				item_data = potato.load.item(item[0], int(item[1]))
				print(item)
				print(item_data)
				time.sleep(2)
				i += 1
			except (urllib.error.HTTPError):
				time.sleep(60)
				item_data = potato.load.item(item[0], int(item[1]))
		x += 1

def main():
	test()
	'''
	item = potato.load.item("MLG Columbus 2016 Challengers (Holo-Foil)", 730)
	print(item)
	
	item_list_json = potato.load.item_list(0, 10)
	item_list = potato.parse.item_list(item_list_json)
	for item in item_list:
		print(item)
	'''

if (__name__ == "__main__"):
	main()
