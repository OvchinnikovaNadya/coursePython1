#Сделать int что 2 + 2 = 5
class MyInt(int):
    def __add__(self,x):
        return super().__add__(x+1)
    
y = MyInt(2)
y += 2
print(y)

#Сделать list в котором не больше 10
x = [1]
print(type(x))

class MyList(list):
    def __init__(self, x):
        if len(x) > 10:
            raise ValueError('Длина list не может быть >10!')
        else:
            super().__init__(x)
    def append(self, x):
        if len(self) == 10:
            raise ValueError('Длина list не может быть >10!')
        else:
            super().append(x)
    
y = MyList([1,2,3,4,5,6,7,8,9,10,11])
print(y)
