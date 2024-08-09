from smartphone import Smartphone

catalog =[]
phone1 = Smartphone("Apple", "iPhone 15", "+79157683211")
phone2 = Smartphone("Samsung", "Galaxy A54", "+79196548976")
phone3 = Smartphone("Xiaomi", "13 Pro", "+79265112321")
phone4 = Smartphone("Asus", "Zenfone 10", "+79653476656")
phone5 = Smartphone("Honor", "10", "+79563988773")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - { phone.model}. {phone.number}")