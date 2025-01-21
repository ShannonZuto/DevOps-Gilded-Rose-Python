from item import Item


class BackstagePasses(Item):
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
            if self.sell_in < 11 and self.quality < 50:
                self.quality += 1
            if self.sell_in < 6 and self.quality < 50:
                self.quality += 1

        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0
