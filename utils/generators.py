import xxhash


def generate_order_hash(order_number):
    try:
        if 99 < order_number < 1000000:
            order_number = str(order_number)
        else:
            return
    except TypeError:
        return
    salt = '1337'
    h = xxhash.xxh32()
    h.update(order_number)
    h.update(salt)
    return h.hexdigest()
