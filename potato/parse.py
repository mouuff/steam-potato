
import urllib.parse
import re
from potato.constants import MARKET_URL

def item_list(json_list):
	'''
	Converts a json list of items to a usable list
	Steam API returns the list of items in a json which contains html
	The role of this function is to parse the html part
	this function should be called after:
	potato.parse.item_list(start, count)
	'''
	html = json_list["results_html"]
	expr = r"href=\"{market_url}/(.*?)/(.*?)\" id=\"resultlink_.\">"
	expr = expr.format(market_url=MARKET_URL)
	regex = re.compile(expr)
	item_tulpe = regex.findall(html)
	item_list = []
	for item in item_tulpe:
		item_name = urllib.parse.unquote(item[1])
		item_list.append([item_name, item[0]])
	return (item_list)
