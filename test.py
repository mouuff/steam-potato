#!/usr/bin/python3

import potato.item
import potato.list
import unittest

RUST = "252490"
ITEMS = [
    ("Reaper Note Pistol", RUST, 74284213),
    ("Lawman", RUST, 86389192)
]

class TestModule(unittest.TestCase):
    def test_list_load(self):
        nb = 5
        list_json = potato.list.load(1, nb)
        for item in list_json:
            print(item["name"])
        self.assertEqual(len(list_json), nb)

    def test_item_price(self):
        for item in ITEMS:
            item_json = potato.item.load_price(*item[0:-1])
            print(item_json)
            self.assertTrue(item_json["success"])

    def test_nameid(self):
        for item in ITEMS:
            nameid = potato.item.load_nameid(*item[0:-1])
            print("nameid : " + str(nameid))
            self.assertTrue(nameid == item[-1])

"""
def reload_item(name, appid, target, debug=True):
    nameid = potato.item.load_nameid(name, appid)
    print(nameid)
    potato.item.load_item_orders_histogram(nameid)
"""

if (__name__ == "__main__"):
    unittest.main()
