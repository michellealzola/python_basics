print('----------------------------------------------------------')
print('MENU:')
print('1 - Insert elements to array')
print('2 - Remove an element')
print('3 - View array')
print('0 - Quit')
print('-----------------------------------------------------------')

user_input = int(input('Enter menu number or press 0 to exit: '))
array = []
while user_input != 0:
    if user_input == 1:
        user_insert = int(input('Enter elements to be inserted (press 99 when done): '))
        while user_insert != 99:
            array.append(user_insert)
            user_insert = int(input('Enter elements to be inserted (press 99 when done): '))
        user_input = int(input('Enter menu number or press 0 to exit: '))
    elif user_input == 2:
        user_remove = int(input('Enter element to be removed: '))
        array.remove(user_remove)
        user_input = int(input('Enter menu number or press 0 to exit: '))
    elif user_input == 3:
        print(array)
        user_input = int(input('Enter menu number or press 0 to exit: '))
