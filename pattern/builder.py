class Car:
    def __init__(self):
        self.wheels = 4
        self.engine = None
        self.seats = None

    class Builder:
        def __init__(self):
            self.car = Car()

        def with_engine(self, engine_type):
            self.car.engine = engine_type
            return self

        def with_seats(self, number_of_seats):
            self.car.seats = number_of_seats
            return self

        def build(self):
            return self.car

# 사용 예시
builder = Car.Builder()
car = builder.with_engine("V8").with_seats(4).build()
print(f"Car with {car.engine} engine and {car.seats} seats.")