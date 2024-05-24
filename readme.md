# tool313

## Overview

This project is a simple command-line tool for generating passwords with various options. Users can specify the desired length of the password and the characters they prefer to include.

## Features

- Generate passwords of varying lengths.
- Choose different types of characters to include in the password.
- Provide an option to specify a custom pattern for the password symbols.

## Usage


1. Open a Terminal or Command Prompt window.
2. Use the following command to run the password generator:

```
python tool313.py <min_length> <max_length> [--upper_case] [--lower_case] [--numbers] [--symbols] [--pattern <pattern>] <file_name>
```

Where:
- `<min_length>`: The minimum length of the password.
- `<max_length>`: The maximum length of the password.
- `--upper_case`: Include uppercase letters in the password (optional).
- `--lower_case`: Include lowercase letters in the password (optional).
- `--numbers`: Include numbers in the password (optional).
- `--symbols`: Include symbols in the password (optional).
- `--pattern <pattern>`: Specify a custom pattern for the password symbols (optional).
- `<file_name>`: The name of the file to save passwords.

4. You will receive a confirmation message after running the command contain the size of generated file.

## Example

To generate a password with 8 to 12 characters, including uppercase and lowercase letters, numbers, symbols, using the pattern "@31" for symbols, and save it to a file named "passwords.txt", you can use the following command:

python tool313.py 8 12 --upper_case --lower_case --numbers --symbols --pattern "@31" passwords.txt


## License

This project is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file.

