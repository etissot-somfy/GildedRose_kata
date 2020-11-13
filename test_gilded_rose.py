# -*- coding: utf-8 -*-
import unittest

from gilded_rose import *
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
  
    def test_backstage_passes_basic(self):
        backstage_pass = BackstagePass(sell_in=20, quality=12)
        rose = GildedRose([backstage_pass])
        rose.update_quality()
        self.assertEqual(backstage_pass.sell_in, 19, "sell_in")
        self.assertEqual(backstage_pass.quality, 13, "quality")

    def test_backstage_passes_less_than_10(self):
        backstage_pass = BackstagePass(sell_in=9, quality=12)
        rose = GildedRose([backstage_pass])
        rose.update_quality()
        self.assertEqual(backstage_pass.sell_in, 8, "sell_in")
        self.assertEqual(backstage_pass.quality, 14, "quality")

    def test_backstage_passes_exactly_10(self):
        backstage_pass = BackstagePass(sell_in=10, quality=12)
        rose = GildedRose([backstage_pass])
        rose.update_quality()
        self.assertEqual(backstage_pass.sell_in, 9, "sell_in")
        self.assertEqual(backstage_pass.quality, 14, "quality")

    def test_backstage_passes_less_than_5(self):
        backstage_pass = BackstagePass(sell_in=4, quality=12)
        rose = GildedRose([backstage_pass])
        rose.update_quality()
        self.assertEqual(backstage_pass.sell_in, 3, "sell_in")
        self.assertEqual(backstage_pass.quality, 15, "quality")
        
if __name__ == '__main__':
    unittest.main()
