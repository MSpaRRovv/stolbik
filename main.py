def stolbik(num, div):
    digits = list(map(int, str(num)))  # число в список цифр

    # Начальные данные в уголке
    print(f"  {num} │ {div}")
    print("-" + " " * len(digits) + "  ├─" + "─" * max(len(str(div)), len(str(num // div))))
    print(" " * len(digits) + f"   │ {num // div}")

    rem = 0  # Начальное значение остатка
    result = ""  # Строка для хранения частного

    for digit in digits:  # Перебираем каждую цифру
        rem = rem * 10 + digit  # Увеличиваем остаток
        if rem >= div:
            res, rem = divmod(rem, div)  # Получаем частное и остаток
            result += str(res)  # Накапливаем частное
            print(f"{'':<{len(result) - 1}}  {res * div:>{len(str(rem))}}")  # Печатаем результат умножения
            print(f"{'':<{len(result) - 1}}──", "─" * len(str(res * div)), sep="")  # Печатаем линию
        else:
            result += '0'  # Если остаток меньше делителя, добавляем '0'

    print(f"{'':<{len(result)}}  {rem}")  # Печатаем остаток
    return int(result) if result else 0, rem  # Возвращаем частное и остаток

# Ввод данных
num = int(input("Введите делимое: "))
div = int(input("Введите делитель: "))

# Вызов функции
result, remainder = stolbik(num, div)
print(f"Частное: {result}, Остаток: {remainder}")
