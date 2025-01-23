#define the menu of restaurant
from functools import total_ordering

menu = ('Pizza :40'
        'Pasta :50'
        'Burger :60'
        'Salad :70'
        'Coffee :80')

#Greet
print("Welcome to Jhalfry Restaurant")
print("Pizza: $40\nPasta: $50\nBurger: $60\nSalad: $70\nCoffee: $80")


item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    print(f"Your item(item_1) has been added to your order")

else:
    print(f"Ordered item(item_1) is not available yet!")

another_order = input("do you want to add another item?(Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        print(f"item (item_2) has been added to order")

    else:
        print("Ordered item is not available!")

print(f"The total amount of items to pay is :", total_ordering)
