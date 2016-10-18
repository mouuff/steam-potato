
import urllib.parse
import urllib.request
import json
from .currency import Currency
from .constants import *

__all__ = ["load_price", "load_nameid"]


def request_json(link, values):
    '''Get json file from steam website
    '''
    request = urllib.parse.urlencode(values)
    url = "{url}?{req}".format(url=link, req=request)
    rep = urllib.request.urlopen(url)
    page = rep.read()
    json_file = json.loads(page.decode('utf-8'))
    return (json_file)


def load_price(name, appid, country=COUNTRY, currency=CURRENCY):
    '''Returns basic item information by name and appid
    appid defines the name of steam game
    it is defined by APPS constant
    '''
    values = {
    "country": country,
    "currency": str(currency.value),
    "appid": str(appid),
    "market_hash_name": name,
    "format": "json"
    }
    json_file = request_json(ITEM_URL, values)
    return (json_file)


def load_nameid(name, appid):
    '''Get the nameid by name
    nameid is useful for order requests
    '''
    url = "{url}/{appid}/{name}".format(url=MARKET_URL,
                                        appid=appid,
                                        name=name)
    print(url)
