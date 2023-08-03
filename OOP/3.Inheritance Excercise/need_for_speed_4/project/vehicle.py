class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: float) -> None:
        needed_fuel = kilometers * self.fuel_consumption

        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel
