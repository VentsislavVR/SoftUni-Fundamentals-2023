from person import Person


class Child(Person):
    pass


person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)


