from menu import products
from collections import Counter


def get_product_by_id(id: int) -> dict:
    if type(id) != int:
        raise TypeError('product id must be an int')
    return next((product for product in products if product["_id"] == id), {})


def get_products_by_type(prod_type: str) -> list[dict]:
    if type(prod_type) != str:
        raise TypeError('product type must be a str')
    return [product for product in products if product['type'] == prod_type]


def add_product(menu: list, **kwargs) -> dict:
    new_item = {
        "_id": max([product['_id'] for product in menu], default=0) + 1,
        **kwargs
    }
    menu.append(new_item)
    return new_item


def menu_report() -> str:
    preco_medio = sum([product['price'] for product in products]) / len(products)
    tipo_mais_comum = Counter([product['type'] for product in products]).most_common(1)[0][0]

    return f"Products Count: {len(products)} - Average Price: ${round(preco_medio, 2)} - Most Common Type: {tipo_mais_comum}"


def add_product_extra(menu: list, *args, **kwargs) -> dict:
    for arg in args:
        if arg not in kwargs:
            raise KeyError(f'field {arg} is required')

    for arg in kwargs.copy():
        if arg not in args:
            kwargs.pop(arg)

    new_item = {
        "_id": max([product['_id'] for product in menu], default=0) + 1,
        **kwargs
    }
    menu.append(new_item)
    return new_item
