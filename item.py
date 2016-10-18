#!/usr/bin/python3

import potato.item
import urllib.error
import time
import re


RUST = "252490"
ITEMS = [
    ("Reaper Note Pistol", RUST, 2.2),
    ("Lawman", RUST, 3.4)
]


def get_lowest_price(item):
    str_lowest_price = item["lowest_price"].replace(",", ".")
    print(str_lowest_price)
    lowest_price = float(re.sub("[^0-9.]", "", str_lowest_price))
    return (lowest_price)


def reload_item(tulpe, debug=True):
    item = potato.item.load_price(tulpe[0], tulpe[1])
    if (item["success"]):
        price = get_lowest_price(item)
        if (debug):
            print("%s\tprice=%f target=%f" % (tulpe[0], price, tulpe[2]))
        if (price <= tulpe[2]):
            return (True)
        return (False)
    if (debug):
        print("%s failed" % (tulpe[0]))
    return (False)


def main():
    for item in ITEMS:
        if (reload_item(item)):
            print("Match")


if (__name__ == "__main__"):
    main()
