# Получаем исходную строку.
# Приводим строку к одному регистру (чтобы игнорировать регистр букв).
# Удаляем из строки все символы, которые не являются буквами или цифрами (чтобы игнорировать пробелы и знаки препинания).
# Сравниваем строку с её перевёрнутой версией.
# Если обе строки совпадают, значит исходная строка — палиндром, иначе — нет.

def is_palindrome(s):

    s = s.lower()

    filtered_chars = [ch for ch in s if ch.isalnum()]
    filtered_str = ''.join(filtered_chars)

    reversed_str = filtered_str[::-1]

    return filtered_str == reversed_str

print(is_palindrome("А роза упала на лапу Азора"))
print(is_palindrome("Привет"))


