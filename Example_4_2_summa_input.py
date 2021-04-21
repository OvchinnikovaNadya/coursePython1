# Задание 4.2. Сумма ряда от 0 до input

import numpy as np
N = int(input('Введите число меньше 100 '))
x = np.array(range(N))

print(np.sum(x))