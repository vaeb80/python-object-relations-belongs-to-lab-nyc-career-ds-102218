# import car class here
from car import Car

class Person:

    _all = []
    _count = 0

    def __init__(self, name, occupation, car=None):
        self._name = name
        self._occupation = occupation
        Person._all.append(self)
        Person._count +=1

    @property
    def name(self):
        return self._name
    @property
    def occupation(self):
        return self._occupation
    @property
    def car(self):
        return self._car
    @car.setter
    def car(self, car):
        self._car = car

    @classmethod
    def has_oldest_car(cls):
        years = [car._year for car in Car.all()]
        for car in Car.all():
            if car._year == min(years):
                return car.owner

    @classmethod
    def drives_a(cls, make):
        people = []
        for person in cls._all:
            if person.car.make == make:
                people.append(person)
        return people

    def drives_same_make_as_me(self):
        make = self.car.make
        people = []
        for person in self._all:
            if person.car.make == make and person != self:
                people.append(person)
        return people
