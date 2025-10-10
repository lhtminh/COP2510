from collections import namedtuple

# Define the MenuItem namedtuple
MenuItem = namedtuple('MenuItem', ['id', 'name', 'price'])

# Global constant for tax
TAX = 0.07

# Menu data
Menu = [
    MenuItem(1, 'Strawberry', 1.25),
    MenuItem(2, 'Mango', 1.50),
    MenuItem(3, 'Banana', 0.95),
    MenuItem(4, 'Yogurt', 1.15),
    MenuItem(5, 'Protein', 1.75)
]

# ------------ begin function definitions ----------------

# Thursday Addition: getinput function
def getinput(prompt, lo, hi):
    valid = False
    while not valid:
        try:
            n = int(input(prompt))
            if n < lo or n > hi:
                print(f'Enter a number between {lo} and {hi}.')
            else:
                valid = True
        except ValueError:
            print('Not a whole number.')
    return n


def show_menu(menu):
    print('\nMenu (press 0 if done): ')
    for item in menu:
        print(f'{item.id}.\t{item.name}\t${item.price:.2f}')


def pick_ing(m):
    chosen = []
    choice = -1  # sentinel

    while choice != 0:
        # get user input 
        choice = getinput('Choose id (Press 0 if done): ', 0, len(m))

        if choice == 0:
            if not chosen:
                print('Add at least one ingredient.')
                choice = -1  # stay in loop
            else:
                break
        else:
            for i in m:
                if i.id == choice:
                    item = i
                    break

            qty = getinput(f'How many {item.name}? ', 1, 5)

            # for loop to build list
            for i in range(qty):
                chosen.append(item)

            print(f'Added {qty} x {item.name}.')
    return chosen  # return a list


def totals(items):
    subtotal = 0
    for i in items:
        subtotal += i.price

    subtotal = round(subtotal, 2)
    tax = round(subtotal * TAX, 2)
    total = round(subtotal + tax, 2)

    return subtotal, tax, total


def main():
    print('Welcome to the Smoothie Bar!')
    show_menu(Menu)
    ingredients = pick_ing(Menu)
    sub, tax, tot = totals(ingredients)

    print('-' * 25)
    print(f'Subtotal: ${sub:.2f}')
    print(f'Tax: ${tax:.2f}')
    print(f'Total: ${tot:.2f}')
    print('Thanks for visiting the smoothie bar!')


main()
