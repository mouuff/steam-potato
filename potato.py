#!/usr/bin/python3

import potato.load
import potato.parse
import urllib.error
import time

def main():
	#test()
	#item = potato.load.item("MLG Columbus 2016 Challengers (Holo-Foil)", 730)
	#print(item)
	
	item_list_json = potato.load.item_list(0, 50)
	#print(item_list_json["results_html"])
	item_list = potato.parse.item_list(item_list_json)
	for item in item_list:
		print(item)

if (__name__ == "__main__"):
	main()
