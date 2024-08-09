from address import Address
from mailing import Mailing


to_address = Address(127550, 'г.Москва', 'Дмитровское шоссе', 29,  1)
from_address = Address(428023, "г.Чебоксары", "ул Гражданская", 54, 7)

mailing = Mailing(to_address, from_address, 1000, 2008765433)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, \
{mailing.from_address.city}, {mailing.from_address.street}, \
{mailing.from_address.house}-{mailing.from_address.apartment} \
в {mailing.to_address.index}, {mailing.to_address.city}, \
{mailing.to_address.street}, {mailing.to_address.house}-{mailing.to_address.apartment}. \
Стоимость {mailing.cost} рублей.")
