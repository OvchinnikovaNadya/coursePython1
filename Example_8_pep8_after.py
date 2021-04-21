# Задание 8. Оформить код по PEP8
from pprint import pprint  # Импорт в отдельной строке

# Функция сравнения 2-х строковых значений
def compare(S1, S2):
    S1, S2 = [
        s.lower() for s in [S1, S2]
    ]
    ngrams = [
        S1[i:i + 3] for i in range(len(S1))
    ]
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    return count / max(len(S1), len(S2))

# Функция обработки исключительной ситуации при получении неверного значения в "s"
# Пытаемся вернуть число из строкового значения "s", если ошибка - сообщаем
def int_val(s):
    try:
        return int(s)
    except ValueError:
        print('Неверное значение: ' + str(s))
        return 0

# Функция тестирования нечеткого сравнения 2-х слов
if __name__ == '__main__':
    for a, b in [
        ('алгоритм', 'алгоритмический'),
        ('стол', 'стул'),
    ]:
        ab = compare(a, b)
    print('Результат теста на сравнение: ', a, b, ab)
print([int_val(s)] for s in ['с', '1'])


# Описание структуры класса Person и его функций
class Person():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.key = (name, address)
    def __repr__(self):
        return "Person('%s','%s','%s')" % (self.name, self.age, self.address)
    def __eq__(self, obj):
        if type(obj) == Person:
            return


#----------Действия с поиском людей в списке
ADRESS_WORDS = {'дом', 'улица', 'живет'}

#Функция сравнения по адресу
def by_address(Q):
    Q = Q - ADRESS_WORDS
    W = set(self.address.split())
    rez = []
    for a, b in product(Q, W):
        rez += [(compare(a, b), a, b)]
    return max(rez)[0]

# Функция обработки возраста из строки в число
def by_age(Q):
    q_age = max([int_val(q) for q in Q])
    if 'старше' in Q:
        return q_age < self.age
    if 'младше' in Q:
        return q_age > self.age
    return q_age + 5 >= self.age >= q_age - 5

# Функция нечеткого сравнения запроса: строка разбивается на слова
def fuzzy_compare(query):
    q = set(query.split())
    score = 0
    for m, a in zip(
            [ADRESS_WORDS, ],
            [by_address, by_name, by_age]):
        if m & q:
            score += f(q)
    return score > 0.49


lena = Person("Елена", 19, "Пушкина, д.10, кв.100")
ivan = Person("Иван", 29, "Пушкина, д.11, кв. 10")
pavel = Person("Павел", 31, "Монастырская, 2, 14")

queries = [
    'имя Иван',
    'возраст 29',
    'живет на Пушкина',
]

people = {
    lena.key: lena,
    ivan.key: ivan,
    pavel.key: pavel,
}
pprint(people)
pprint(people[ivan.key])
