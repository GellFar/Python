from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Тверская", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Невский", "20", "15")

mailing = Mailing(to_address, from_address, 250, "TRK123456789")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.town}, "
      f"{mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartament} "
      f"в {mailing.to_address.index}, {mailing.to_address.town}, "
      f"{mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartament}. "
      f"Стоимость {mailing.cost} рублей.")
