from abc import ABC, abstractmethod
import logging
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)

# Логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Клас Vehicle
class Vehicle(ABC):
    def __init__(self, make: str, model: str, region_spec: str):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


# Клас Car, успадковує Vehicle
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(
            f" {Fore.BLUE}{self.make} {self.model} ({self.region_spec} Spec): {Style.BRIGHT}Двигун запущено"
        )


# Клас Motorcycle, успадковує Vehicle
class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(
            f" {Fore.YELLOW}{self.make} {self.model} ({self.region_spec} Spec): {Style.BRIGHT}Мотор заведено"
        )


# Абстрактний клас VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


# Фабрика для US
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US")


# Фабрика для EU
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU")


# Приклад
if __name__ == "__main__":
    # Фабрика для US
    us_factory = USVehicleFactory()
    us_car = us_factory.create_car("Chevrolet", "Impala 1967")
    us_motorcycle = us_factory.create_motorcycle("Indian", "Challenger")

    us_car.start_engine()
    us_motorcycle.start_engine()

    # Фабрика для EU
    eu_factory = EUVehicleFactory()
    eu_car = eu_factory.create_car("Volkswagen", "Touareg")
    eu_motorcycle = eu_factory.create_motorcycle("BMW", "R 1250 RT")

    eu_car.start_engine()
    eu_motorcycle.start_engine()
