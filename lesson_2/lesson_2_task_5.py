def month_to_season(m):
    if m in(1, 2, 12):
        return("Зима")
    elif m in(3, 4, 5):
        return("Весна")
    elif m in(6, 7, 8):
        return("Лето")
    elif m in(9, 10, 11):
            return("Осень")
    else:
        return("Укажите правильный номер месяца")
print(month_to_season(int(input("Введите номер месяца "))))



