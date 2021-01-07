from unittest import TestCase

from shopping_cart.cart import Cart


class TestCart(TestCase):

    def setUp(self) -> None:
        self.blackCat = 'black cat'
        self.hsinchu = 'hsinchu'
        self.postOffice = 'post office'
        self.cart = Cart()

    def test_black_cat_with_light_weight(self):
        shipping_fee = self.shipping_fee(self.blackCat, 30, 20, 10, 5)
        self.feeShouldBe(150, shipping_fee)

    def test_black_cat_with_heavy_weight(self):
        shipping_fee = self.shipping_fee(self.blackCat, 30, 20, 10, 50)
        self.feeShouldBe(500, shipping_fee)

    def test_hsinchu_with_small_size(self):
        shipping_fee = self.shipping_fee(self.hsinchu, 30, 20, 10, 50)
        self.feeShouldBe(144, shipping_fee)

    def test_hsinchu_with_huge_size(self):
        shipping_fee = self.shipping_fee(self.hsinchu, 100, 20, 10, 50)
        self.feeShouldBe(480, shipping_fee)

    def test_post_office_by_weight(self):
        shipping_fee = self.shipping_fee(self.postOffice, 100, 20, 10, 3)
        self.feeShouldBe(110, shipping_fee)

    def test_post_office_by_size(self):
        shipping_fee = self.shipping_fee(self.postOffice, 100, 20, 10, 300)
        self.feeShouldBe(440, shipping_fee)

    def shipping_fee(self, shipper, length, width, height, weight):
        shipping_fee = self.cart.shipping_fee(shipper, length, width, height, weight)
        return shipping_fee

    def feeShouldBe(self, expected, actual_fee):
        self.assertEqual(expected, actual_fee)
