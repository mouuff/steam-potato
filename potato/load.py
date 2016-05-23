
import urllib.parse
import urllib.request
#from . import constants
from potato.constants import COUNTRY, CURRENTY, AGENTS, PRICE_URL

def item(name, appid, country=COUNTRY, currency=CURRENTY):
	agents = {"User-Agent" : AGENTS}
	values = {
	"country" : country,
	"currenty" : str(currency),
	"appid" : str(appid),
	"market_hash_name" : name
	}
	request = urllib.parse.urlencode(values)
	url = "{url}?{req}".format(url=PRICE_URL, req=request)
	rep = urllib.request.urlopen(url)
	print(rep.read())
