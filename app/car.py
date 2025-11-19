import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_way(self,
                 start_curd: list[int, int],
                 target_curd: list[int, int],
                 fuel_price: int | float) -> int | float:
        catenary_1 = start_curd[0] - target_curd[0]
        catenary_2 = start_curd[1] - target_curd[1]
        distance = math.sqrt((catenary_1 ** 2) + (catenary_2 ** 2))
        return self.fuel_consumption * distance / 100 * fuel_price
