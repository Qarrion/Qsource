class TransportFactory:
    class Truck:
        def deliver(self):
            return "Delivering by land in a truck."

    class Ship:
        def deliver(self):
            return "Delivering by sea in a ship."

    @staticmethod
    def get_transport(mode):
        if mode == 'land':
            return TransportFactory.Truck()
        elif mode == 'sea':
            return TransportFactory.Ship()
        else:
            raise ValueError("Invalid mode of transport")

# 사용 예시
factory = TransportFactory()
truck = factory.get_transport('land')
print(truck.deliver())  # "Delivering by land in a truck."

ship = factory.get_transport('sea')
print(ship.deliver())  # "Delivering by sea in a ship."