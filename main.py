s = input("""Вводите в правильном формате используя пробелы, пример "2 + 2" ,каждая операнда должна быть не более числа 10 и не равна 0: """)


def main(input: str):
    str_split = input.split()
    if len(str_split) < 3:
        raise NameError('т.к. строка не является математической операцией или неправильный формат')
    if len(str_split) > 3:
        raise NameError('т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)')
    if not str_split[0].isdigit() or not str_split[0].isdigit() or int(str_split[0]) > 10 or int(str_split[2]) > 10 or int(str_split[0]) <= 0 or int(str_split[2]) <= 0:
        raise Exception('т.к. операнда является не целым числом, больше числа 10 или равна 0')

    arithmetic_dict = {'-': int(str_split[0]) - int(str_split[2]),
                       '+': int(str_split[0]) + int(str_split[2]),
                       '*': int(str_split[0]) * int(str_split[2]),
                       '/': int(str_split[0]) / int(str_split[2]),
                       }

    if str_split[1] in arithmetic_dict:
        print(arithmetic_dict[str_split[1]])
    else:
        raise NameError('Непредвиденная ошибка')


if __name__ == '__main__':
    main(s)

# 2-2
# 2 - 2
# 2- 2

#10-10
#10 -10
#10 - 10
