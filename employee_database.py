# M0_C7 - Employee Database
########################################
# Modify and debug the code as needed. #
########################################
import sys

usage = '''Usage: [COMMAND] [ID]
    add    [ID] - Add a new employee record
    edit   [ID] - Edit an employee record
    view   [ID] - View an employee record
    remove [ID] - Delete an employee record
    exit        - Exits
'''

names = {}
cities = {}

def add_employee_record(id_num, name, city):
    """Adds an employee record if record doesn't already exist
    and values are not empty.

    Arguments:
    id_num -- ID of employee record to add
    name   -- Name of employee. Cannot be empty
    city   -- City of employee. Cannot be empty
    """

    # If ID already exists, return False
    if id_num in names or id_num in cities:
        return False

    # If name or city are empty, return False
    if not name or not city:
        return False

    # Otherwise create the dictionary pairs
    names[id_num] = name
    cities[id_num] = city

    return True

def edit_employee_record(id_num, name, city):
    """Edits an employee record if it exists.

    Arguments:
    id_num -- ID of employee record to edit
    name   -- New name to change to
    city   -- New city to change to
    """
    if not id_num in names or not id_num in cities:
        return False

    if name:
        names[id_num] = name
    if city:
        cities[id_num] = city

    return True

def get_employee_record(id_num):
    """Gets an employee's details if record exists.

    Arguments:
    id_num -- ID of employee record to fetch
    """
    if not id_num in names or not id_num in cities:
        return 'Error viewing record'

    return f'{id_num} {names[id_num]} {cities[id_num]}'

def remove_employee_record(id_num):
    """Deletes an employee's records if they exist.

    Arguments:
    id_num -- ID of employee record to remove
    """
    if id_num in names:
        del names[id_num]
    else:
        return False
    if id_num in cities:
        del cities[id_num]
    else:
        return False

    return True

if __name__ == '__main__':
    print(usage)
    err = '>> Invalid command'

    while True:
        command = input('<< ')
        cmd_arr = command.split()
        if len(cmd_arr) == 1 and cmd_arr[0] == 'exit':
            sys.exit('>> Exiting')
        elif len(cmd_arr) == 2:
            try:
                id_num = int(cmd_arr[1])
                if cmd_arr[0] == 'add':
                    name = input('Name << ')
                    city = input('City << ')
                    # Hint: Look up python ternary
                    print('>> Record added' if add_employee_record(id_num, name, city) else '>> Error adding record')
                elif cmd_arr[0] == 'edit':
                    name = input('Name << ')
                    city = input('City << ')
                    print('>> Record edited' if edit_employee_record(id_num, name, city) else '>> Error editing record')
                elif cmd_arr[0] == 'view':
                    result = get_employee_record(id_num)
                    print(f'>> {result}' if result else '>> Error viewing record')
                elif cmd_arr[0] == 'remove':
                    print('>> Record removed' if remove_employee_record(id_num) else '>> Error removing record')
                else:
                    print(err)
            except ValueError:
                print('>> Invalid ID')
        else:
            print('>> Invalid command')
