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


def reload_item(name, appid, target, debug=True):
    nameid = potato.item.load_nameid(name, appid)
    print(nameid)
    potato.item.load_item_orders_histogram(nameid)

def main():
    for item in ITEMS:
        if (reload_item(*item)):
            print("Match")


if (__name__ == "__main__"):
    main()
