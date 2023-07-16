def calculate_total_price(cart):
    itens = cart["items"]
    precos = itens[1::2]  # LISTAR APENAS OS PREÇOS
    cart = sum(precos)
    return cart
