#!/usr/bin/python3

import potato.load
import potato.parse
import urllib.error
import time

def get_diff(item_data):
	diff = 0.0
	try:
		low = item_data["lowest_price"].replace("€", "").replace(",", ".")
		med = item_data["median_price"].replace("€", "").replace(",", ".")
		flow = float(low)
		fmed = float(med)
		diff = fmed - flow
		#print(diff)
	except:
		pass
	return (diff)
		

def test():
	max_diff = 0.0
	max_name = ""
	x = 0
	while (x < 1000):
		item_list_json = potato.load.item_list(x + 400, 100)
		item_list = potato.parse.item_list(item_list_json)
		i = 0
		while (i < len(item_list)):
			item = item_list[i]
			try:
				item_data = potato.load.item(item[0], int(item[1]))
				if (get_diff(item_data) > max_diff):
					max_name = item[0]
					max_diff = get_diff(item_data)
					print("NEW MAX DIFF = " + str(max_diff))
				print(item)
				print(item_data)
				i += 1
			except (urllib.error.HTTPError):
				time.sleep(60)
				item_data = potato.load.item(item[0], int(item[1]))
		x += 100

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
