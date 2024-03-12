import pytest
from task_1.task1 import Cart, Product


@pytest.fixture(autouse=True)
def sample_products():
    p1 = Product('borjomi','water', 2)
    p2 = Product('milka','candy', 3)
    p3 = Product('tabasco','souse', 4)
    p4 = Product('kozel','beer', 1)
    return p1, p2, p3, p4


def test_add_products(sample_products):
    customer_cart = Cart()
    p1, p2, p3, p4 = sample_products
    customer_cart.add_products(p1, 2)
    customer_cart.add_products(p2, 3)
    customer_cart.add_products(p4, 2)
    customer_cart.add_products(p3, 1)
    assert customer_cart.products == {p1:2, p2:3, p3:1, p4:2}
    
def test_total_price(sample_products):
    customer_cart = Cart()
    p1, p2, p3, p4 = sample_products
    customer_cart.add_products(p1, 2)
    customer_cart.add_products(p2, 3)
    customer_cart.add_products(p4, 2)
    customer_cart.add_products(p3, 1)
    assert customer_cart.total_price() == 19
    
def test_iadd(sample_products):
    customer_cart1 = Cart()
    customer_cart2 = Cart()
    p1, p2, p3, p4 = sample_products
    customer_cart1.add_products(p1, 2)
    customer_cart1.add_products(p2, 3)
    customer_cart2.add_products(p4, 2)
    customer_cart2.add_products(p3, 1)
    customer_cart1 += customer_cart2
    assert customer_cart1.products == {p1:2, p2:3, p3:1, p4:2}    
    
def test_iter(sample_products):
    customer_cart = Cart()
    p1, p2, p3, p4 = sample_products
    customer_cart.add_products(p1, 2)
    customer_cart.add_products(p2, 3)
    customer_cart.add_products(p4, 2)
    customer_cart.add_products(p3, 1)
    count = 0
    for product, amount in customer_cart:
        assert isinstance(product, Product)
        assert isinstance(amount, int)
        count += 1
    assert count == 4