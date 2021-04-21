# Задание 6.2. Реализовать поиск по полям типа рост больше 120, имя Наташа
from pprint import pprint
class Person():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.key = (name, address)
    def __repr__(self):
        return "Person('%s','%s','%s')" % (self.name, self.age, self.address)

def search(x):
    for i in people:
        if x ==
        print('Наташа найдена')
    else:
        print("Данное имя не найдено: " + str(x))

lena = Person("Елена", 19, "Пушкина, д.10, кв.100")
ivan = Person("Иван", 29, "Пушкина, д.11, кв. 10")
natasha = Person("Наташа", 27, "Ленина, д.8, кв. 13")
pavel = Person("Павел", 31, "Монастырская, 2, 14")
people = {
    lena.key: lena,
    ivan.key: ivan,
    natasha.key: natasha,
    pavel.key: pavel,
}
pprint(people)
pprint(people[natasha.key])

people.search('Наташа')
