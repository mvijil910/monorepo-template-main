# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
    
    def test_conjured_item(self):
        # Arrange
        items = [Item("Conjured", 5, 42)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Conjured")
        original_quality = gr.get_item_quality("Conjured")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Conjured")
        new_quality = gr.get_item_quality("Conjured")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality < original_quality
        assert new_quality == original_quality - 2

    def test_conjured_item2(self):
        # Arrange
        items = [Item("Conjured", -2, 42)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Conjured")
        original_quality = gr.get_item_quality("Conjured")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Conjured")
        new_quality = gr.get_item_quality("Conjured")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality < original_quality
        assert new_quality == original_quality - 4

    def test_sulfuras_item(self):
        # Arrange
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 49)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Sulfuras, Hand of Ragnaros")
        original_quality = gr.get_item_quality("Sulfuras, Hand of Ragnaros")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Sulfuras, Hand of Ragnaros")
        new_quality = gr.get_item_quality("Sulfuras, Hand of Ragnaros")

        assert new_sell_in == original_sell_in

        assert new_quality == 80

    def test_bkstg_item(self):
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 46)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert")
        original_quality = gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert")
        new_quality = gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality > original_quality
        assert new_quality == original_quality + 3
    def test_bkstg_item2(self):
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 13)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert")
        original_quality = gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert")
        new_quality = gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality < original_quality
        assert new_quality == 0
        
    def test_bkstg_item3(self):
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert")
        original_quality = gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert")
        new_quality = gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality > original_quality
        assert new_quality == original_quality + 2
        
    def test_agedBrie_item(self):
        # Arrange
        items = [Item("Aged Brie", 0, 50)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Aged Brie")
        original_quality = gr.get_item_quality("Aged Brie")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Aged Brie")
        new_quality = gr.get_item_quality("Aged Brie")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality == original_quality
        assert new_quality == original_quality
        
    

if __name__ == '__main__':
    unittest.main()
