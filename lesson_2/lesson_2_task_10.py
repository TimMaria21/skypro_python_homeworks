def bank(x,y):
    for each_year in range (y):
         x += (x * 0.1)
    return x

x = float(input("Сумма Вашего вклада? "))

y = int(input("На какой срок? "))

print("Сумма на вашем счету будет = ", bank(x, y), "спустя", y, "лет")