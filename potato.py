#!/usr/bin/python3

import potato.load

def main():
	#item = potato.load.item("Chroma 2 Case Key", 730)
	#print(item)
	
	item_list = potato.load.item_list(0, 3)
	print(item_list["results_html"])

if (__name__ == "__main__"):
	main()
