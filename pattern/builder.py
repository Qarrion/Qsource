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


# ---------------------------------------------------------------------------- #'
# 중첩 클래스인 A와 B에서 Myclass의 메소드를 직접 호출할 수는 없지만, 
# Myclass의 인스턴스를 내부에 포함시켜 이를 가능하게 할 수 있습니다.
# 이렇게 하려면, A와 B 클래스 내부에 Myclass의 인스턴스를 생성하고, 
# 이 인스턴스를 통해 Myclass의 메소드에 접근합니다. 이 방법은 컴포지션
# (composition)이라고 불리며, 클래스가 다른 클래스의 기능을 내부적으로 
# 사용하는 방법입니다.

class Myclass:
    # 공통적으로 사용할 변수
    common_variable = "공통 값"

    def common_method(self):
        print("Myclass의 공통 메소드")

    class A:
        def __init__(self):
            self.myclass_instance = Myclass()
            print(f"A 클래스 인스턴스 생성, 공통 변수: {Myclass.common_variable}")
        
        def main_function(self):
            print("A 클래스의 main_function")
            self.myclass_instance.common_method()

    class B:
        def __init__(self):
            self.myclass_instance = Myclass()
            print(f"B 클래스 인스턴스 생성, 공통 변수: {Myclass.common_variable}")

        def main_function(self):
            print("B 클래스의 main_function")
            self.myclass_instance.common_method()

# Myclass의 A와 B 클래스를 인스턴스화
myclass_a = Myclass.A()
myclass_b = Myclass.B()

# 인스턴스의 메서드 사용
myclass_a.main_function()
myclass_b.main_function()