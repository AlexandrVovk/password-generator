import secrets
import string


def main(password_length = 15) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation

    dubious_special_chars = ['!', '|', '\\', '/',  '`', "'", ';', ':' ,',', '.']
    dubious_letters = ['l', 'i', 'I', 'O', 'o']
    dubious_digits = ['1', '0']
    dubious = dubious_special_chars + dubious_letters + dubious_digits
    
    for item in dubious:
        alphabet = alphabet.replace(item, '')

    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    return password

if __name__ == "__main__":
    print(main())
