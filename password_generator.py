import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""

# Запрашиваем сколько паролей нужно сгенерировать
pass_amount = int(input("Введите числовое значение - количество паролей для генерации"))

# Запрашиваем длину пароля
pass_length = int(input("Введите числовое значение - длину пароля с помощью числа:"))


# Объявляем функцию защиты от дурака
def is_true(ans):
    while ans != "Y" and ans != "N":
        ans = input("Введите Y или N:")
    return ans


is_num = input("Использовать цифры 0-9? Введите Y если да, N если нет:")
is_number = is_true(is_num)

is_upp = input("Использовать прописные буквы A-Z? Введите Y если да, N если нет:")
is_upper_letters = is_true(is_upp)

is_lower = input("Использовать строчные буквы a-z? Введите Y если да, N если нет:")
is_lower_letters = is_true(is_lower)

is_punct = input("Использовать символы !#$%&*+-=?@^_? Введите Y если да, N если нет:")
is_punctuation = is_true(is_punct)

is_ex = input("Исключать неоднозначные символы il1Lo0O? Введите Y если да, N если нет:")
is_exception = is_true(is_ex)

# К переменной chars добавляем все символы, допустимые в генерируемом пароле
if is_number == "Y":
    chars += digits
if is_upper_letters == "Y":
    chars += uppercase_letters
if is_lower_letters == "Y":
    chars += lowercase_letters
if is_punctuation == "Y":
    chars += punctuation
if is_exception == "Y":
    for_removing = "il1Lo0O"
    for c in for_removing:
        chars = chars.replace(c, "")


# Объявляем функцию, которая создает пароль заданной длины из рандомных символов из заданного списка
def generate_password(length, chars):
    password = ""
    for i in range(length):
        password += chars[random.randrange(len(chars))]
    return password


# Выводим запрошенное пользователем количество сгенерированных паролей
for i in range(pass_amount):
    password = generate_password(pass_length, chars)
    print(password)
