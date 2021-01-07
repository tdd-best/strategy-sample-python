class Product(object):
    def __init__(self, length, width, height, weight) -> None:
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length


class Cart:
    def __init__(self):
        self.shipping_fee_funcs = {
            'black cat': Cart.fee_by_black_cat,
            'hsinchu': Cart.fee_by_hsinchu,
            'post office': Cart.fee_by_post_office,
        }

    def shipping_fee(self, shipper, product):
        if shipper in self.shipping_fee_funcs:
            return self.shipping_fee_funcs[shipper](product)
        else:
            raise ValueError('shipper not exist')

    @staticmethod
    def fee_by_post_office(product):
        fee_by_weight = 80 + product.weight * 10
        size = product.length * product.width * product.height
        fee_by_size = size * 0.00002 * 1100
        return min(fee_by_size, fee_by_weight)

    @staticmethod
    def fee_by_hsinchu(product):
        size = product.length * product.width * product.height
        if product.length > 100 or product.width > 100 or product.height > 100:
            return size * 0.00002 * 1100 + 500
        else:
            return size * 0.00002 * 1200

    @staticmethod
    def fee_by_black_cat(product):
        if product.weight > 20:
            return 500
        else:
            return 100 + product.weight * 10
