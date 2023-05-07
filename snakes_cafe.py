menu = ['Cookies', 'Salmon', 'Steak', 'Meat Tornado', 'Spring Rolls']
# list comprehension which creates list of tuples
order_counts = [(item, 0) for item in menu]


def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Items :-
----------
Cookies
Salmon
Steak
Meat Tornado
Spring Rolls


***********************************
** What would you like to order? **
***********************************
''')

def Snaks():
    intro()
    user_input = ''
    while user_input.lower() != 'quit':
        user_input = input('> ').title().strip()
        # cheack if the input NOT empty
        if user_input != '':
            if user_input in menu:
                index = menu.index(user_input)
                item, count = order_counts[index]
                order_counts[index] = (item, count + 1)
                print(f'** {count + 1} order of {item} have been added to your meal **')
            else:
                print('Sorry, we don\'t have this item!')

    end_application()


def end_application():
    print('Thanks for using the Snakes Cafe application!')


if __name__ == '__main__':
    Snaks()


