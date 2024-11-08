from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Engine started")


class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Engine started")


class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model + " (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model + " (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model + " (EU Spec)")

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model + " (EU Spec)")


def main():
    us_vehicle_factory = USVehicleFactory()
    ford_mustang = us_vehicle_factory.create_car("Ford", "Mustang")
    hd_sportster = us_vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
    ford_mustang.start_engine()
    hd_sportster.start_engine()

    eu_vehicle_factory = EUVehicleFactory()
    renault_megane = eu_vehicle_factory.create_car("Renault", "Megan")
    adler_eagle = eu_vehicle_factory.create_motorcycle("Adler", "The Eagle")
    renault_megane.start_engine()
    adler_eagle.start_engine()


if __name__ == "__main__":
    main()
