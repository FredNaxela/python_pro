import exceptions_list
import clients
import menu_of_dishes
import discounts_list


if __name__ == '__main__':
    dish1 = menu_of_dishes.Dish('Salad Cesar', 'chicken, iceberg, tomato', 10)
    dish2 = menu_of_dishes.Dish('Pasta Carbonara', 'spaghetti, eggs, cheese, bacon', 12)
    dish3 = menu_of_dishes.Dish('Cheesecake', 'cheese philadelphia, lemon jam', 5)

    menu = {
        'Appetizers': menu_of_dishes.MenuCategory('Appetizers'),
        'Main Dishes': menu_of_dishes.MenuCategory('Main Dishes'),
        'Desserts': menu_of_dishes.MenuCategory('Desserts')
    }

    menu['Appetizers'].add_dish(dish1)
    menu['Main Dishes'].add_dish(dish2)
    menu['Desserts'].add_dish(dish3)

    print()
    print(menu['Appetizers'])
    print(menu['Main Dishes'])
    print(menu['Desserts'])
    print()

    try:
        client1 = clients.Client('Ivan', discounts_list.RegularDiscount())
        client2 = clients.Client('Anna', discounts_list.SilverDiscount())
        client3 = clients.Client('Mark', discounts_list.GoldDiscount())
    except exceptions_list.IncorrectDiscount as e:
        print(e)


    order1 = [dish1, dish2]
    order2 = [dish2, dish3]
    order3 = [dish1, dish3]
    order1 += [dish3]
    order2 += [dish1]
    
    print()
    for dish in order2:
        print(dish)
    
   
    print()
    print(f'{client1} total price: {client1.get_total_price(order1)}$')
    print(f'{client2} total price: {client2.get_total_price(order2)}$')
    print(f'{client3} total price: {client3.get_total_price(order3)}$')