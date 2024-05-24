import argparse
import os
import string

def generate_passwords(characters, min_length, max_length):
    def generate_password(length):
        if length == 0:
            return ['']
        return [char + password for char in characters for password in generate_password(length - 1)]

    return [password for length in range(min_length, max_length + 1) for password in generate_password(length)]

def main():
    parser = argparse.ArgumentParser(description='Generate passwords and save them to a file.')
    parser.add_argument('min_length', help='The minimum length of the password', type=int)
    parser.add_argument('max_length', help='The maximum length of the password', type=int)
    parser.add_argument('--upper_case', help='Include uppercase letters', action='store_true')
    parser.add_argument('--lower_case', help='Include lowercase letters', action='store_true')
    parser.add_argument('--numbers', help='Include numbers', action='store_true')
    parser.add_argument('--symbols', help='Include symbols', action='store_true')
    parser.add_argument('--pattern', help='Specify a pattern for the password symbols', type=str)
    parser.add_argument('list_name', help='The name of the file to save passwords', type=str)
    args = parser.parse_args()

    if args.min_length > 8 and args.max_length > 8 :
        print('warning that will drive to generate a "BIG FILE SIZE"')
        
    charset = ''

    if args.upper_case:
        charset += string.ascii_uppercase

    if args.lower_case:
        charset += string.ascii_lowercase

    if args.numbers:
        charset += string.digits

    if args.symbols:
        charset += string.punctuation

    # Check if the user specified a pattern for password symbols
    if args.pattern:
        charset += args.pattern

    if not charset:
        print("Error: You must specify at least one character set.")
        return

    generate_passwords_to_file(charset, args.min_length, args.max_length, args.list_name)

def generate_passwords_to_file(characters, min_length, max_length, filename):

    with open(filename, 'w') as file:
        for password in generate_passwords(characters, min_length, max_length):
            file.write(password + '\n')

    file_size = os.path.getsize(filename)

    file_size_kb = file_size / 1024

    if file_size_kb < 1024:
        print(f'The size of the file is {file_size_kb:.2f} KB')
    else:
        file_size_mb = file_size_kb / 1024
        print(f'The size of the file is {file_size_mb:.2f} MB')

if __name__ == "__main__":
    main()
