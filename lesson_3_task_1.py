
from User import User

# Создание нового экземпляра User
my_user = User("Максим", "Миронов")

# Вызов всех методов у объекта my_user
my_user.sayName()  # Печатает имя
my_user.sayLast()   # Печатает фамилию
my_user.fullName()   # Печатает и то и другое
