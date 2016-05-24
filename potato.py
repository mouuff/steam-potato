#!/usr/bin/python3

import potato.load
import potato.parse

def main():
	#item = potato.load.item("Chroma 2 Case Key", 730)
	#print(item)
	
	item_list = potato.load.item_list(0, 3)
	potato.parse.item_list(item_list)

if (__name__ == "__main__"):
	main()
