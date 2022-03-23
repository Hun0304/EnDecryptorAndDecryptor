from random import randint
from math import floor
from typing import Tuple, List

prime_dict = {0: 37, 1: 41, 2: 43, 3: 47, 4: 53, 5: 59, 6: 61, 7: 67, 8: 71, 9: 73, 10: 79,
              11: 83, 12: 89, 13: 97, 14: 101, 15: 103, 16: 107, 17: 109, 18: 113}


def decrypt(cipher_text, rand, list) -> str:
    print(f'密文: {cipher_text}')
    index = 0
    list_temp = list
    print(list_temp)
    char_values = []
    mod_values = []
    values = []
    keys = []
    quo_values = []
    plain_text = ''
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if i % 2 == 0:
            char_values.append(char)
            key = ord(char)
            keys.append(key)
            value = [k for k, v in prime_dict.items() if v == key]
            values.append(*value)
            quo_value = values[index] + 19 * list_temp[index]
            quo_values.append(quo_value)
            index += 1
        else:
            if char == '@':
                char = '0'
            mod_values.append(int(char))
            # key = 19 * rand + int(char)
    for i in range(len(list_temp)):
        ascii_value = quo_values[i] * rand + mod_values[i]
        plain_text += chr(ascii_value)

    print(f'Quotient: {quo_values}')
    print(f'Values: {values}')
    print(f'Keys: {keys}')
    print(f'Char: {char_values}')
    print(f'Modulo: {mod_values}')
    print(f'Plain_Text: {plain_text}')

    return plain_text


def encrypt(plain_text, rand) -> Tuple[str, List[int]]:
    cipher_text = ''
    ascii_values = []
    mod_values = []
    quo_values = []
    char_values = []
    char_quo_values = []
    print(f'明文: {plain_text}')
    print(f'Random: {rand}')
    for character in plain_text:
        ascii_values.append(ord(character))       # Ascii = Quotient * rand + Modulo
        quo_value = floor(ord(character) / rand)  # Quotient
        mod_value = ord(character) % rand         # Modulo
        char_quo_value = floor(quo_value / 19)
        char_quo_values.append(char_quo_value)
        char = chr(prime_dict[(quo_value % 19)])
        quo_values.append(quo_value)
        if mod_value == 0:
            mod_value = '@'
        mod_values.append(mod_value)
        char_values.append(char)
        cipher_text += (char + str(mod_value))
    print(f'Char Quotients: {char_quo_values}')
    print(f'Ascii: {ascii_values}')
    print(f'Quotient: {quo_values}')
    print(f'Char: {char_values}')
    print(f'Modulo: {mod_values}')
    print(f'密文: {cipher_text}')

    return cipher_text, char_quo_values


def main() -> None:
    plain_text = '狂賀！光世代4/1起降價　292萬戶受惠'
    rand = randint(1, 10)
    print('加密流程...')
    cipher_text, list = encrypt(plain_text, rand)
    print('---------------------------------')
    print('解密流程...')
    decrypt(cipher_text, rand, list)

    return None


if __name__ == '__main__':
    main()
