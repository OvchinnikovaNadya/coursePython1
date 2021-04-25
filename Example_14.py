class People(dict):
    def __compare__(self, s1, s2):
        count = 0
        for ngram in ( s1[i:i+3] for i in range(len(s1)) ):
            count += s2.count(ngram)
        
        return count / max(len(s1),len(s2)) > 0.5
        
    def __getitem__(self, k1):
        for k2, v in self.items():
            if self.__compare__(k1, k2):
                return v
                
    def update(self, obj):
        super().update({obj.key:obj})
        
class Person:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr
        
        self.key = name
    
    def __repr__(self):
        return "Person('%s',%s,'%s')" % (self.name, self.age, self.addr)
        
if __name__ == '__main__':
    masha = Person('маша', 19, 'пушкина')
    glasha = Person('глаша', 23, 'мушкина')
    
    people = People()
    people.update(masha)
    people.update(glasha)
    print(people)
    print(people['мааша'])