from AgedBrie import AgedBrie
from BackstagePasses import BackstagePasses
from Sulfuras import Sulfuras
from item import Item


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()