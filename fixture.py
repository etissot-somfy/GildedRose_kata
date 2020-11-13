from gilded_rose import *

class Fixture:
    items = [
            [BaseItem(name="+5 Dexterity Vest", sell_in=10, quality=20), BaseItem(name="+5 Dexterity Vest", sell_in=9, quality=19)],
            [BrieItem(sell_in=2, quality=0),BrieItem(sell_in=1, quality=1)],
            [BaseItem(name="Elixir of the Mongoose", sell_in=5, quality=7), BaseItem(name="Elixir of the Mongoose", sell_in=4, quality=6)],
            [Sulfuras(sell_in=0, quality=80), Sulfuras(sell_in=0, quality=80)],
            [Sulfuras(sell_in=-1, quality=80), Sulfuras(sell_in=-1, quality=80)],
            [BackstagePass(sell_in=15, quality=20), BackstagePass(sell_in=14, quality=21)],
            [BackstagePass(sell_in=10, quality=49), BackstagePass(sell_in=9, quality=50)],
            [BackstagePass(sell_in=5, quality=49), BackstagePass(sell_in=4, quality=50)],
            [BackstagePass(sell_in=10, quality=40), BackstagePass(sell_in=9, quality=42)],
            [BackstagePass(sell_in=5, quality=40), BackstagePass(sell_in=4, quality=43)],
            [BaseItem(name="Conjured Mana Cake", sell_in=3, quality=6), BaseItem(name="Conjured Mana Cake", sell_in=2, quality=4)]
    ]

    def get_items_for_day(self, day):
        result = []
        for item in Fixture.items:
            result.append(item[day])
        return result

    def get_initial(self):
        return self.get_items_for_day(0)

