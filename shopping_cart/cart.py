class Cart:
    def shipping_fee(self, shipper, length, width, height, weight):
        if shipper == 'black cat':
            if weight > 20:
                return 500
            else:
                return 100 + weight * 10
        elif shipper == 'hsinchu':
            size = length * width * height
            if length > 100 or width > 100 or height > 100:
                return size * 0.00002 * 1100 + 500
            else:
                return size * 0.00002 * 1200
        elif shipper == 'post office':
            fee_by_weight = 80 + weight * 10;
            size = length * width * height;
            fee_by_size = size * 0.00002 * 1100;
            return fee_by_weight if fee_by_weight < fee_by_size else fee_by_size;
        else:
            raise ValueError('shipper not exist')
