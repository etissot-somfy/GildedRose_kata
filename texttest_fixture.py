# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

from fixture import Fixture

if __name__ == "__main__":
    print("OMGHAI!")
    fixture = Fixture()
    days = 2
    items = fixture.get_items_for_day(0)
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
