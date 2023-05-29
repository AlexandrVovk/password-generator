import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
password_length = 15

def main() -> str:
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    password_length = 15

    dubious_special_chars = ['!', '|', '\\', '/',  '`', "'", ';', ':' ,',', '.']
    for item in dubious_special_chars:
        special_chars = special_chars.replace(item, '')

    dubious_letters = ['l', 'i', 'I', 'O', 'o']
    for item in dubious_letters:
        letters = letters.replace(item, '')

    dubious_digits = ['1', '0']
    for item in dubious_digits:
        digits = digits.replace(item, '')

    alphabet = letters + special_chars + digits
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    return password

if __name__ == "__main__":
    print(main())
