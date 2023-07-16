def apply_discount(cart, discount):
    for i in range(1, len(cart), 2):
        original_price = cart[i]
        discounted_price = original_price - (original_price * discount)
        cart[i] = discounted_price
        return cart