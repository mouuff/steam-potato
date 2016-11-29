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
        lowest = float(data["lowest_sell_order"]) / 100
        highest = float(data["highest_buy_order"]) / 100
        diff = lowest - highest
        print("%.2f | %f | %f" % ((diff / lowest) * 100, lowest, highest))
    else:
        print("Error")


def item_get_price(item):
    str_price = item["sale_price"]
    price_filter = filter(lambda x: x.isdigit() or x == ".", str_price)
    price = "".join(price_filter)
    return (float(price))


def main():
    items = potato.list.load(5, 100, "252490")
    for item in items:
        price = item_get_price(item)
        if (price < 1.5 and price > 0.1):
            reload_item(item["name"], item["appid"])
            time.sleep(15)
            # must wait to prevent ban


if (__name__ == "__main__"):
    main()
