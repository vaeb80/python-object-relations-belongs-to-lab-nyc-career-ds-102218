class Car:

    _all = []


    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        owner.car = self
        Car._all.append(self)

    @classmethod
    def all(cls):
        return cls._all
    @property
    def model(self):
        return self._model
    @property
    def owner(self):
        return self._owner
    @property
    def make(self):
        return self._make
    @property
    def year(self):
        return self._year


    @owner.setter
    def owner(self, owner):
        owner.car = self
        self._owner = owner

    @classmethod
    def cars_driven_by(cls, occupation):
        cars = []
        for car in cls._all:
            if car.owner.occupation == occupation:
                cars.append(car)
        return cars
