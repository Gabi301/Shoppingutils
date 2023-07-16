def calculate_total_price(cart):
    itens = produtos["items"]
    precos = itens[1::2]  # LISTAR APENAS OS PREÇOS
    valor_total = sum(precos)
    return valor_total