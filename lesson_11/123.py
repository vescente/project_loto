class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = new_age

    def __str__(self):
        return f'Person age: {self._age}'


lep = Person(25)
print(lep.age)
lep.age = 32
print(lep.age)
print(lep)
