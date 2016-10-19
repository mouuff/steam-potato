
import urllib.parse
import urllib.request
import json
import re
from .currency import Currency
from .constants import *

__all__ = ["load_price", "load_nameid", "load_item_orders_histogram"]


def request_json(link, values):
    '''Get json file from link
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
    quoted_name = urllib.parse.quote(name)
    url = "{url}/{appid}/{name}".format(url=MARKET_URL,
                                        appid=appid,
                                        name=quoted_name)
    rep = urllib.request.urlopen(url)
    html = rep.read()
    expr = r"Market_LoadOrderSpread\( ([0-9]*) \);"
    result = re.findall(expr, html.decode("utf-8"))
    if (result):
        return (int(result[0]))
    return (0)


def load_item_orders_histogram(nameid,
                               country="FR",
                               currency=CURRENCY,
                               language="english",
                               two_factor=0):
    '''Get the item orders histogram
    with sell and buy orders
    Returns a json file from steam, content needs to be parsed
    '''
    values = {
    "country": country,
    "language": language,
    "currency": str(currency.value),
    "item_nameid": str(nameid),
    "two_factor": str(two_factor)
    }
    json_file = request_json(ITEM_ORDERS_HISTOGRAM, values)
    return (json_file)
