#!/usr/bin/python3

import potato.item
import potato.list
import urllib.error
import time
import re


def reload_item(name, appid):
    print("-" * 10)
    print(name)
    nameid = potato.item.load_nameid(name, appid)
    data = potato.item.load_item_orders_histogram(nameid)
    if (data):
        lowest = float(data["lowest_sell_order"])
        highest = float(data["highest_buy_order"])
        print("price: " + str(lowest / 100))
        print((lowest - highest) / 100)
    else:
        print("Error")


def main():
    items = potato.list.load(1, 100)
    for item in items:
        reload_item(item["name"], item["appid"])
        time.sleep(10)
        # must wait to prevent ban


if (__name__ == "__main__"):
    main()
