
import urllib.parse
import re
from potato.constants import MARKET_URL

def item_name(html):
	'''
	Get item name and appid
	'''
	expr = r"href=\"{market_url}/(.*?)/(.*?)\" id=\"resultlink_"
	expr = expr.format(market_url=MARKET_URL)
	appid, name = re.findall(expr, html)[0]
	name = urllib.parse.unquote(name)
	return (name, appid)

def html_get_span(html, name):
	'''
	Get span from name
	this function is used to get normal price, sale, price
	'''
	expr = r'<span class=\"{name}\">(.*?)</span>'.format(name=name)
	span = re.findall(expr, html)
	return (span[0])

def html_item(html):
	'''
	Get item information from html
	this function should be called after
	potato.parse.item_list(json_list) function
	returns a dictionary of containing item informations:
	name, appid, normal_price, sale_price, quantity
	'''
	name, appid = item_name(html)
	normal_price = html_get_span(html, "normal_price")
	sale_price = html_get_span(html, "sale_price")
	quantity = html_get_span(html, "market_listing_num_listings_qty")
	info = {
	"name" : name,
	"appid" : appid,
	"normal_price" : normal_price,
	"sale_price" : sale_price,
	"quantity" : quantity
	}
	return (info)

def item_list(json_list):
	'''
	Converts a json list of items to a usable list
	Steam API returns the list of items in a json which contains html
	The role of this function is to parse the html part
	this function should be called after:
	potato.parse.item_list(start, count)
	'''
	html = json_list["results_html"]
	html_classes = re.findall(r'<a ((.|\n)*?)</a>', html)
	result = []
	for html_class in html_classes:
		result.append(html_item(html_class[0]))
	return (result)
