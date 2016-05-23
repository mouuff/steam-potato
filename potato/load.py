
import urllib.parse
import urllib.request
import json
from potato.constants import COUNTRY, CURRENTY, ITEM_URL, LIST_URL

def request_json(link, values):
	request = urllib.parse.urlencode(values)
	url = "{url}?{req}".format(url=link, req=request)
	rep = urllib.request.urlopen(url)
	page = rep.read()
	json_file = json.loads(page.decode('utf-8'))
	return (json_file)

def item_json(name, appid, country=COUNTRY, currency=CURRENTY):
	values = {
	"country" : country,
	"currenty" : str(currency),
	"appid" : str(appid),
	"market_hash_name" : name,
	"format" : "json"
	}
	json_file = request_json(ITEM_URL, values)
	return (json_file)

def item_list_json(start, count):
	values = {
	"start" : str(start),
	"count" : str(count),
	"format" : "json"
	}
	json_file = request_json(LIST_URL, values)
	return (json_file)
