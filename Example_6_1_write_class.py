# Задание 6.1. Описать классом мои данные
from pprint import pprint
class Person():
    def __init__(self, name, age, address):
        self.name = name 
        self.age = age
        self.address = address
        self.key = (name, address)
    def __repr__(self):
        return "Person('%s','%s','%s')" % (self.name, self.age, self.address)

lena = Person("Елена", 19, "Пушкина, д.10, кв.100")
ivan = Person("Иван", 29, "Пушкина, д.11, кв. 10")
pavel = Person("Павел", 31, "Монастырская, 2, 14")
people = {
    lena.key: lena,
    ivan.key: ivan,
    pavel.key: pavel,
}
pprint(people)
pprint(people[ivan.key])

