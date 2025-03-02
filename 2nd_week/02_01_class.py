class Person:
    def __init__(self, param):
        print(f'hihi {param['name']} created', self)
        self.name = param['name']

    def talk(self):
        print(f'hello my name is {self.name}')

person_1 = Person({"name":'Taeseop'})
person_1.talk()

person_2 = Person({"name":'Seth'})
person_2.talk()