from menu import products


def calculate_tab(dict_list: list) -> dict:

    valor_total = sum([
        product['price'] * item['amount']
        for item in dict_list
        for product in products
        if product["_id"] == item['_id']
    ])

    return {'subtotal': f'${round(valor_total, 2)}'}
