class Bak:
    def __init__(self, fuel_type, fuel_count):
        self.fuel_type = fuel_type
        self.fuel_count = fuel_count

    def up(self, count):
        self.fuel_count += count

    def down(self, count):
        if self.fuel_count<count:
            self.fuel_count = 0
        else:
            self.fuel_count -= count


class Vehicle:

    def __init__(self, bak):
        self.bak = bak

    def add_fuel(self, count):
        self.bak.up(count)

    def drive(self, distance, fuel_consumption_map):
        if self.bak.fuel_count >= distance/fuel_consumption_map[self.bak.fuel_type]:
            self.bak.down(distance/fuel_consumption_map[self.bak.fuel_type])
            print(f"Мы проехали весь путь: {distance} КМ.  ",f'Бензина осталось: {self.bak.fuel_count}')
        elif self.bak.fuel_count == 0:
            print("Бензина нет!!!")
        else:
            distance_we_can_go = self.bak.fuel_count * fuel_consumption_map[self.bak.fuel_type]
            self.bak.down(self.bak.fuel_count)
            print(f"Мы проехали часть пути: {distance_we_can_go} КМ.  ",f'Бензина осталось: {self.bak.fuel_count}')


a = fuel_consumption_map = {
        "GAS": 1,
        "B93": 1.5,
        "B94": 2,
        "ELC": 3,
    }



bak1 = Bak("ELC", 100)
car = Vehicle(bak1)

bak2 = Bak("B94", 200)
bus = Vehicle(bak2)

car.drive(150, a)
car.drive(100, a)
car.drive(50, a)
bus.drive(175, a)
bus.drive(250, a)





