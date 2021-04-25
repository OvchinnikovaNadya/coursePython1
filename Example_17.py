# Задание 17. Исключения для классов
class AddressException(Exception):
    pass


class TooManyPeopleException(AddressException):
    pass


class MaleMaleException(AddressException):
    pass


class FemaleFemaleException(AddressException):
    pass


class PersonAlreadyHasAddress(AddressException):
    pass


# Описание структуры базового класса Person и его функций (checkin - вселение для Мужчин и Женщин, а также с проверкой, что могут жить вместе)
class Person:
    def checkin(self, address):
        if not self._has_address:
            address.move_in(self)
            self._has_address = 1
        else:
            raise PersonAlreadyHasAddress()

    def __init__(self, a_name):
        self._name = a_name
        self._has_address = 0

    def can_live_with(self, other):
        if len(other) > 1:
            raise TooManyPeopleException()


# Описание структуры класса-потомка Мужчин и его функций
class Male(Person):
    def __repr__(self):
        return "\u2642(%s)" % self._name

    def can_live_with(self, other):
        super().can_live_with(other)
        try:
            if type(other[0]) == Male:
                raise MaleMaleException()
        except IndexError:
            pass


# Описание структуры класса-потомка Женщин и его функций
class Female(Person):
    def __repr__(self):
        return "\u2640(%s)" % self._name

    def can_live_with(self, other):
        super().can_live_with(other)
        if other and other[0] == Female:
            raise FemaleFemaleException()

# Описание структуры класса Адреса и его функций (movi_in - заселение; is_occupied - уже живут по этому адресу)
class Address:
    def __init__(self, label):
        self.__label = label
        self.__tenants = []

    def move_in(self, person):
        try:
            person.can_live_with(self.__tenants)
            self.__tenants += [person]
        except Exception as e:
            raise e

    def is_occupied(self):
        return len(self.__tenants) > 0

    def people(self):
        return self.__tenants

    def __repr__(self):
        return "\u2302(%s, %s)" % (self.__label, self.__tenants)


from itertools import product
from sys import stderr

if __name__ == '__main__':
    for address, person in product((Address('A'),
                                    Address('B')),
                                   (Male("Вася"), # Создаем 4-х людей (2 мужчины и 2 женщины)
                                    Male("Паша"),
                                    Female("Лена"),
                                    Female("Катя"))):
        try:
            person.checkin(address)
            print(person, address)
        except Exception as e:
            print(type(e), person, address, file=stderr)