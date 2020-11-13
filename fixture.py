from gilded_rose import *

class Fixture:
    items = [
            [Item(name="+5 Dexterity Vest", sell_in=10, quality=20), Item(name="+5 Dexterity Vest", sell_in=9, quality=19)],
            [Item(name="Aged Brie", sell_in=2, quality=0),Item(name="Aged Brie", sell_in=1, quality=1)],
            [Item(name="Elixir of the Mongoose", sell_in=5, quality=7), Item(name="Elixir of the Mongoose", sell_in=4, quality=6)],
            [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)],
            [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)],
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20), Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=14, quality=21)],
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49), Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=50)],
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49), Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=50)],
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=40), Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=42)],
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=40), Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=43)],
            [Item(name="Conjured Mana Cake", sell_in=3, quality=6), Item(name="Conjured Mana Cake", sell_in=2, quality=4)]
    ]

    def get_items_for_day(self, day):
        result = []
        for item in Fixture.items:
            result.append(item[day])
        return result

    def get_initial(self):
        return self.get_items_for_day(0)

