class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center: float = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income: float = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rate: int) -> None:
        total_rating: float = (self.average_rating
                               * self.count_of_ratings + rate)
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


bmw = Car(3, 3, "BMW")
audi = Car(4, 9, "Audi")

print(bmw.clean_mark)

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6,
)

income = wash_station.serve_cars([bmw, audi])

print(income)
print(bmw.clean_mark)

bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(comfort_class=4, clean_mark=2, brand="Audi")

print(bmw.clean_mark)
print(audi.clean_mark)

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6,
)

income = wash_station.serve_cars([bmw, audi])
print(income)
print(bmw.clean_mark)
print(audi.clean_mark)

wash_station = CarWashStation(
    distance_from_city_center=6,
    clean_power=8,
    average_rating=3.9,
    count_of_ratings=11,
)

print(wash_station.average_rating)
print(wash_station.count_of_ratings)

wash_station.rate_service(5)

print(wash_station.average_rating)
print(wash_station.count_of_ratings)

bmw = Car(3, 3, "BMW")
audi = Car(4, 9, "Audi")
mercedes = Car(7, 1, "Mercedes")

ws = CarWashStation(6, 8, 3.9, 11)

income = ws.serve_cars([bmw, audi, mercedes])

print(income == 41.7)

print(bmw.clean_mark == 8)
print(audi.clean_mark == 9)
print(mercedes.clean_mark == 8)

ford = Car(2, 1, "Ford")
wash_cost = ws.calculate_washing_price(ford)
print(wash_cost == 9.1)
print(ford.clean_mark == 1)

ws.rate_service(5)

print(ws.count_of_ratings == 12)
print(ws.average_rating == 4.0)
