class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cost = ((car.comfort_class * (self.clean_power - car.clean_mark)) *
                        (self.average_rating / self.distance_from_city_center))
                income += round(cost, 1)
                car.clean_mark = self.clean_power
        return round(income, 1)

    def calculate_washing_price(self, car) -> float:
        return ((car.comfort_class * (self.clean_power - car.clean_mark)) *
                (self.average_rating / self.distance_from_city_center))

    def wash_single_car(self, car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        self.average_rating = (self.average_rating + rate) / 2
        self.count_of_ratings += 1
