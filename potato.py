#!/usr/bin/python3

import potato.load
import potato.parse

def main():
	item = potato.load.item("MLG Columbus 2016 Challengers (Holo-Foil)", 730)
	print(item)
	
	item_list_json = potato.load.item_list(0, 10)
	item_list = potato.parse.item_list(item_list_json)
	for item in item_list:
		print(item)

if (__name__ == "__main__"):
	main()
