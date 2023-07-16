from shoppingutils import *

itens_carrinho = ["Arroz", 3,
        "Azeite", 1,
        "Café", 2,
        "Extrato de tomate", 4,
        "Feijão", 3,
        "Macarrão", 4]

stock = {"Arroz": 15,
        "Azeite": 10,
        "Café": 10,
        "Extrato de tomate": 8,
        "Feijão": 10,
        "Macarrão": 15}


check_avalability(itens_carrinho, stock)