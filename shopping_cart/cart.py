class Product(object):
    def __init__(self, length, width, height, weight) -> None:
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length


class Cart:
    @staticmethod
    def shipping_fee(shipper, t_length, t_width, t_height, t_weight):
        product = Product(t_length, t_width, t_height, t_weight)
        if shipper == 'black cat':
            if product.weight > 20:
                return 500
            else:
                return 100 + product.weight * 10
        elif shipper == 'hsinchu':
            size = product.length * product.width * product.height
            if product.length > 100 or product.width > 100 or product.height > 100:
                return size * 0.00002 * 1100 + 500
            else:
                return size * 0.00002 * 1200
        elif shipper == 'post office':
            fee_by_weight = 80 + product.weight * 10
            size = product.length * product.width * product.height
            fee_by_size = size * 0.00002 * 1100
            return min(fee_by_size, fee_by_weight)
        else:
            raise ValueError('shipper not exist')
