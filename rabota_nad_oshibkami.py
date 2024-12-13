
### Третий вариан, если последний символ "0", то возвращает "1" для удаления Нуля в конце строки:

def get_multiplied_digits(number):
    str_number = str(number)

    for i in range(len(str_number)):
            first = int(str_number[0])
            if len(str_number) > 1:
                return first * get_multiplied_digits(int(str_number[1:]))
            end = int(str_number[-1])
            if end == 0:
                return 1
            else:
                return first

print(get_multiplied_digits(40203))

result2 = get_multiplied_digits(402030007600)
print(result2)

result_3 = get_multiplied_digits(870887323000)
print(result_3)