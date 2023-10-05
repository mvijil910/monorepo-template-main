# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
    
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


if __name__ == '__main__':
    unittest.main()
