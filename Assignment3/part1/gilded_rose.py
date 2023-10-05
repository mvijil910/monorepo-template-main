# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
    
    def update_quality(self):
        
        def update_qual_conjured(qual, sell_in):
            if qual < 50: 
                if qual > 0:
                    if sell_in > 0: 
                        if qual > 2: 
                            qual = qual - 2
                        elif qual == 1: 
                            qual = qual -1
                        else: 
                            qual = 0
                        return qual
                    else: 
                        if qual > 4: 
                            qual = qual - 4
                        return qual 
                else: 
                    return 0    
            return 50
        
        def update_qual_agedBrie(qual): 
            if qual < 50:
                qual = qual + 1
            return qual 
        
        def update_qual_bkstg(sellIn, qual): 
            if qual < 50:
                if sellIn < 11:
                    if sellIn < 0: 
                        qual = 0
                    elif sellIn < 6:
                        qual += 3
                    else: 
                        qual += 2
                    return qual
            elif qual == 50: 
                qual = 50
            return qual 
        
        def update_qual_sulfuras(qual):
            qual = 80
            return qual
        
        for item in self.items: 
            if item.name != "Sulfuras, Hand of Ragnaros": 
                item.sell_in = item.sell_in - 1
            if item.name == "Aged Brie": 
                item.quality = update_qual_agedBrie(item.quality)
            elif item.name == "Sulfuras, Hand of Ragnaros": 
                item.quality = update_qual_sulfuras(item.quality)
            elif item.name == "Conjured": 
                item.quality = update_qual_conjured(item.quality, item.sell_in)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert": 
                item.quality = update_qual_bkstg(item.sell_in, item.quality)
                if item.quality > 50: 
                    item.quality = 50    
            else: 
                if item.quality > 0 and item.quality <= 50 and item.sell_in > 0: 
                    item.quality = item.quality - 1
                elif item.sell_in < 0: 
                    item.quality = item.quality - 2
                
                              
    
    def get_item_sell_in(self, itemName): 
        for item in self.items: 
            if itemName == item.name: 
                return item.sell_in
    
    def get_item_quality(self, itemName): 
        for item in self.items: 
            if itemName == item.name:
                return item.quality