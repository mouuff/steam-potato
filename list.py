#!/usr/bin/python3

import potato.list
import urllib.error
import time
import re

STEP = 100


def load_list_loop():
    '''Example of item listing'''
    x = 0
    while (x < STEP * 10):
        try:
            item_list = potato.list.load(x, STEP)
            print("Loaded {x} items at {range}".format(x=STEP, range=x))
            for item in item_list:
                print(item)
            x += STEP
        except (urllib.error.HTTPError):
            print("HTTP Error")
            time.sleep(10)
        time.sleep(5)


def main():
    load_list_loop()

if (__name__ == "__main__"):
    main()
