#!/usr/bin/python3

import potato.load
import potato.parse
import urllib.error
import time
import re

STEP = 100

def get_price_diff(item):
	normal_price = item["normal_price"]
	sale_price = item["sale_price"]
	normal_price = re.findall(r'\$(.*) USD', normal_price)[0]
	sale_price = re.findall(r'\$(.*) USD', sale_price)[0]
	return (float(normal_price) - float(sale_price))

def test():
	diff_max = 0
	item_max = None
	x = 0
	while (x < STEP * 100):
		try:
			item_list = potato.load.item_list(x, STEP)
			print("Loaded {x} items at {range}".format(x=STEP, range=x))
			#print(item_list_json["results_html"])
			#item_list = potato.parse.item_list(item_list_json)
			for item in item_list:
				print(item)
				if (get_price_diff(item) > 1):
					diff_max = get_price_diff(item)
					item_max = item
					print("NEW DIFF:")
					print(item)
					print(diff_max)
				#print(get_price_diff(item))
			
			x += STEP
		except (urllib.error.HTTPError):
			print("429 Error")
			time.sleep(5)

def main():
	test()
	

if (__name__ == "__main__"):
	main()
