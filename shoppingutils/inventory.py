def check_avalability(cart, inventory):
    for produto_stock, quantidade_stock in inventory.items():
        quantidade_carrinho = sum(cart[1::2]) # soma os valores de uma lista
        quantidade_stock = sum(inventory.values()) # soma os valores de um dicionario 
    if quantidade_stock > quantidade_carrinho:
        return True
    else:
        return False

