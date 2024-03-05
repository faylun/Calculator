import os, time as t

def show_introduction():
    print('=-'*15)
    print(f'\n{" " * 8} Calculator\n')
    print('=-'*15)
    t.sleep(2)

def operation():
    os.system('cls')

    while True:
        print('''
=================================== 
                
    [ 1 ] - Sum
    [ 2 ] - Subtraction
    [ 3 ] - Multiplication
    [ 4 ] - Division
    [ 0 ] - Exit
        
===================================           
        ''')

        user = int(input('Select a option: '))

        match user:
            case 1:
                first_value = float(input('\nFirst value: '))
                second_value = float(input('Second value: '))

                print(f'\n{first_value} + {second_value} = {(first_value + second_value):.2f}')
            case 2:
                first_value = float(input('\nFirst value: '))
                second_value = float(input('Second value: '))

                print(f'\n{first_value} - {second_value} = {(first_value - second_value):.2f}')
            case 3:
                first_value = float(input('\nFirst value: '))
                second_value = float(input('Second value: '))

                print(f'\n{first_value} * {second_value} = {(first_value * second_value):.2f}')
            case 4:
                first_value = float(input('\nFirst value: '))
                second_value = float(input('Second value: '))

                if second_value == 0:
                    print('\nInvalid Operation.')
                else:
                    print(f'\n{first_value} / {second_value} = {(first_value / second_value):.2f}')
            case 0:
                break
        option_user = ''
        while True:
            option_user = str(input('\nDo you wanna continue? [ Y / N ] ')).lower()[0]

            if option_user in ('y', 'n'):
                break

            print("Invalid input. Please enter 'y' or 'n'.")

        if option_user == 'n':
            break
        os.system('cls')
    print('\nBye ;)\n')



show_introduction()
operation()