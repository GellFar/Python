from smartphone import Smartphone

Catalog = [
    Smartphone("Apple", "iPhone 14", "+79012345678"),
    Smartphone("Samsung", "Galaxy S21", "+79098765432"),
    Smartphone("Xiaomi", "Mi 11", "+79123456789"),
    Smartphone("Google", "Pixel 6", "+79234567890"),
    Smartphone("OnePlus", "9 Pro", "+79345678901")
]

for smartphone in Catalog:
    print(f"{smartphone.mark_t} - {smartphone.model_t}, {smartphone.num_t}")
