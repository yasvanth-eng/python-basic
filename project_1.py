ice_cream_shop = []


def view_menu():
    menu = [
        "vanilla       --- 320Rs",
        "chocolate     --- 380Rs",
        "strawberry    --- 300Rs",
        "blueberry     --- 250Rs",
        "mango         --- 230Rs",
        "orange        --- 230Rs",
    ]

    print("--- ICE CREAM MENU ---")

    for item in menu:
        print(item)


def register_flavour():
    menu = ["vanilla", "chocolate", "strawberry", "blueberry", "mango", "orange"]
    flavour = input("Enter the flavour :")
    if flavour in menu:
        print("order registered")
    else:
        print("flavour not found")
    registered_flavour = {
        "flavour registered": flavour,
    }
    ice_cream_shop.append(registered_flavour)


def view_registered_flavour():
    print("-" * 85)
    print("view flavour")
    print("-" * 85)

    if len(ice_cream_shop) == 0:
        print("No students registered yet.")
        return
    for index, registered_flavour in enumerate(ice_cream_shop, 1):
        print("-" * 85)

        print("registered flavour:", registered_flavour["flavour registered"])

        print("-" * 85)


def view_bill():
    bill = {
        "vanilla": 320,
        "chocolate": 380,
        "strawberry": 300,
        "blueberry": 250,
        "mango": 230,
        "orange": 230,
    }

    for flavour, price in bill.items():
        print(f"{flavour}: {price}Rs")



while True:
    print()
    print("1. view menu")
    print("2. register flavour")
    print("3. view registered flavour")
    print("4. view the bill")
    print("5. exit website")
    print("-" * 85)

    choice = int(input("Enter your choice :"))

    if choice == 1:
        view_menu()
    elif choice == 2:
        register_flavour()
    elif choice == 3:
        view_registered_flavour()
    elif choice ==4:
        view_bill()
    elif choice == 5:
        break
    else:
        ("invalid choice")
        break
