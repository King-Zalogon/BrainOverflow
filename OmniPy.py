"""
Helpful things created to ease my work and, hopefully, maybe one day somebody else's
"""


def use_file(filename, data=None, mode=None, encode='utf-8', func=None, *args, **kwargs):
    file = filename
    if not check_for_file(file):
        print('File not found.')
        answer = input('Do you want to create it? Y/N: ')[0].lower()
        if answer == 'y':
            create_file(file, encode)
        else:
            print('Ok, bye')
    else:
        print(f'File "{file}" ready')
        input('Press "ENTER" to continue: ')

    if data is not None:
        answer = input('Do you want to add the data to it? Y/N: ')[0].lower()
        if answer == 'y':
            write_to_file(file, data, encode = encode)
        else:
            print('Ok, bye')


# Check if a file already exists #
def check_for_file(filename):

    try:
        with open(filename, "r") as file:
            file.seek(0)
            content = file.read()

    except FileNotFoundError:
        return False

    else:
        return True


# Creates a files is it doesn't exist already #
def create_file(filename, encode):
    if not check_for_file(filename):
        try:
            with open(filename, 'w', encoding=encode) as file:
                file.write('')
        except FileExistsError:
            print('Error caught')
        else:
            print(f'File "{filename}" created 1')
    else:
        print(f'File "{filename}" already exists')


# Writes to a text file #
def write_to_file(filename, data, mode='a', encode='utf-8'):

    try:
        with open(filename, mode, encoding=encode) as file:
            file.write(f'\n{data}')
            # file.write(data)
    except:
        print('Error caught while trying to write into file')
    else:
        print('Data added to file')


# Reads from a text file #
def read_file(filename):

    with open(filename, "r") as file:
        content = file.read()
        print(content)


# Replace existing content in a text file #
def replace_in_file(filename, current_text, new_text, encode='utf-8'):
    with open(filename, "r+", encoding=encode) as file:
        content = file.read()
        modified_content = content.replace(current_text, new_text)
        file.seek(0)  # Moves the file pointer to the beginning of the file
        file.write(modified_content)
        file.truncate()  # If the modified content is shorter than the original, truncate the file


file_name = 'test_file.txt'
my_data = f'Another string in the {file_name}'

use_file(file_name)


def list_of_primes(limit):
    # using the sieve of Eratosthenes method
    primes = []
    is_prime = [True] * (limit + 1)

    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return primes
