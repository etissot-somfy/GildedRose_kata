# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from fixture import Fixture

class GildedRoseTest(unittest.TestCase):
    def test_loop_items(self):
        fixture = Fixture()
        rose = GildedRose(fixture.get_initial())
        rose.update_quality()
        for item in Fixture.items:
            self.assertEqual(item[0].name,item[1].name, "Bad name :{}".format(item[0].name))
            self.assertEqual(item[0].quality,item[1].quality, "Unexpected quality for : {}".format(item[0].name))
            self.assertEqual(item[0].sell_in,item[1].sell_in, "Unexpected Sell_in for : {}".format(item[0].name)) 

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
    


if __name__ == '__main__':
    unittest.main()
