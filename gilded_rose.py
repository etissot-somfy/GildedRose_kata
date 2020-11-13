# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    ITEM_VEST = "+5 Dexterity Vest"
    ITEM_BRIE = "Aged Brie"
    ITEM_ELIXIR = "Elixir of the Mongoose"
    ITEM_SULFURAS = "Sulfuras, Hand of Ragnaros"
    ITEM_BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    ITEM_MANA_CAKE = "Conjured Mana Cake"

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class BaseItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name=name, sell_in=sell_in, quality=quality)
        self.conjured = name.startswith('Conjured')

    def update_quality(self):
        if self.conjured:
            self.quality = self.quality - 2
        else:
            self.quality = self.quality - 1
        self.quality = max(self.quality, 0)

class BrieItem(Item):
    def __init__(self, sell_in, quality):
        Item.__init__(self, name=Item.ITEM_BRIE, sell_in=sell_in, quality=quality)

    def update_quality(self):
        self.quality = min(self.quality + 1, 50)

class Sulfuras(Item):
    def __init__(self, sell_in, quality):
        Item.__init__(self, name=Item.ITEM_SULFURAS, sell_in=sell_in, quality=quality)

    def update_quality(self):
        self.quality = max(min(self.quality, 50), 0)

class BackstagePass(Item):
    def __init__(self, sell_in, quality):
        Item.__init__(self, name=Item.ITEM_BACKSTAGE_PASS, sell_in=sell_in, quality=quality)

    def update_quality(self):
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 6:
            self.quality = self.quality + 3
        elif self.sell_in < 11:
            self.quality = self.quality + 2
        else:
            self.quality = self.quality + 1
        self.quality = min(self.quality, 50)