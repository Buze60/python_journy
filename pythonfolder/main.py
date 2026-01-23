class Cart:
   def __init__(self):
       self.items = []

   def add(self, item):
       self.items.append(item)

   def remove(self, item):
       if item in self.items:
           self.items.remove(item)
       else:
           print(f'{item} is not in cart')

   def list_items(self):
       return self.items

   def __len__(self):
       return len(self.items)

   def __getitem__(self, index):
       return self.items[index]

   def __contains__(self, item):
       return item in self.items

   def __iter__(self):
       return iter(self.items)
   
   
cart = Cart()

print('W E L C O M E  T O  Y O U R  S H O P P I N G M A L L😊')

choice = int(input('press 1-5 to continue shopping or exit:\n1. Add item\n2. Remove item\n3. View cart items\n4. View cart size\n5. View Item in the cart\n6. Exit\n'))

while choice != 6:
    if choice == 1:
        item = input("Enter item to add: ")
        cart.add(item)
        print(f"{item} added to cart.")
    elif choice == 2:
        item = input("Enter item to remove: ")
        cart.remove(item)
    elif choice == 3:
        print("Cart items:", cart.list_items())
    elif choice == 4:
        print("Cart size:", len(cart))
    elif choice == 5:
        item_contained = cart.__contains__(input('Enter item to check if it is in cart:'))
        if item_contained == True:
            print(f"Item is in the cart. {item_contained}")
        else:
            print("Item is not found in the cart!. ")
    else:
        print("Invalid choice.")

    choice = int(input('press 1-6 to continue shopping or exit:\n1. Add item\n2. Remove item\n3. View cart items\n4. View cart size\n6. Exit\n'))

