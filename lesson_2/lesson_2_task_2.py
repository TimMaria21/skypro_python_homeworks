is_year_leap = int(input("Введите год: "))
year = is_year_leap
def is_year_leap():
    if year % 4 == 0:
        print("Год", year, ":", True)
    else:
        print("Год", year, ":", False)
is_year_leap()