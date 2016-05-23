
import urllib.parse
import urllib.request
import json
from potato.constants import COUNTRY, CURRENTY, ITEM_URL

def item(name, appid, country=COUNTRY, currency=CURRENTY):
	values = {
	"country" : country,
	"currenty" : str(currency),
	"appid" : str(appid),
	"market_hash_name" : name
	}
	request = urllib.parse.urlencode(values)
	url = "{url}?{req}".format(url=ITEM_URL, req=request)
	rep = urllib.request.urlopen(url)
	page = rep.read()
	json_file = json.loads(page.decode('utf-8'))
	return (json_file)
