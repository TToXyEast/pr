import math


def cipher_diavola(text, encrypt_key):
    eng_low_start = ord('a')
    eng_low_end = ord('z')
    eng_upp_start = ord('A')
    eng_upp_end = ord('Z')
#инициализация переменной
    ciphered = ''

    for cipher_symbol in text:

        # код символа
        code_symbol = ord(cipher_symbol)
      #диапозон от начала с +1 значением ибо выводится не все
        if code_symbol in range(eng_low_start, eng_low_end + 1) \
                or code_symbol in range(eng_upp_start, eng_upp_end + 1):

            new_code = code_symbol + encrypt_key

            if eng_low_end < new_code < eng_low_end + encrypt_key + 1:
                new_code = eng_low_start + (new_code - eng_low_end - 1)

            if eng_upp_end < new_code < eng_upp_end + encrypt_key + 1:
                new_code = eng_upp_start + (new_code - eng_upp_end - 1)

            cipher_symbol = chr(new_code)
                 #  cipher+cipher_symbol
        ciphered += cipher_symbol

    return ciphered


if __name__ == '__main__':


    # открываем исходный файл  на чтение
    with open('input.txt', 'r') as f_inp:
        encrypted = cipher_diavola(f_inp.read(), 4)
        # открываем encrypted.txt на запись

    with open('encrypted.txt', 'w') as f_out:
        f_out.write(encrypted)

