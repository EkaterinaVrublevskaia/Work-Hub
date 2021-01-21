#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
# name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar,
# SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.s = speed
        self.c = color
        self.n = name
        self.i = is_police
        #is_police = False

    def go(self):
        return f"Пассажиры машины {self.n}, пристегнитесь, мы поехали!"

    def stop(self):
        return f"Машина {self.n}, остановка!"

    def turn(self, direction):
        return f"Машина {self.n}, поворот на {direction}"
        #i = input("Введите в какую сторону вы хотите повернуть: '>' - на право, '<' - на лево: ")
        #if i == '>':
        #    print(f"Машина {self.n}, поворот направо!")
        #elif i == '<':
        #    print(f"Машина {self.n}, поворот налево!")

    def show_speed(self):
        return f"Ваша текущая скорость {self.s}"


class TownCar(Car):

    def __init__(self, speed, color, name, family=True):
        super().__init__(speed, color, name)
        self.f = family

    def show_speed(self):
        if self.s > 60:
            print(f'Вы превысили скорость!\nВаша скорость {self.s}.\nСнизьте скорость ниже 60.')
        elif self.s <= 60:
            return f"Ваша скорость {self.s}"


class SportCar(Car):
    def __init__(self, speed, color, name, speed_l=True):
        super().__init__(speed, color, name)
        self.s = speed_l


class WorkCar(Car):
    def __init__(self, speed, color, name, work_car=True):
        super().__init__(speed, color, name)
        self.w = work_car

    def show_speed(self):
        if self.s > 40:
            print(f"Вы превысили скорость!\nВаша скорость сейчас {self.s}.\nСнизьте скорость до 40.")
        elif self.s <= 40:
            return self.s


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def chase(self):
        return f"Пришел сигнал на перехват. Включаются мигалки."



town_car = TownCar(70, "Red", "KIA Rio")
print(town_car.s, town_car.c, town_car.n, town_car.i)
print(town_car.go())
print(town_car.show_speed())
print(town_car.turn('Направо'))
print(town_car.stop())
sport_car = SportCar(200, "Black", "BMW M4")
print(sport_car.s, sport_car.c, sport_car.n, sport_car.i)
print(sport_car.go(), sport_car.turn('Налево'), sport_car.show_speed(), sport_car.stop())
work_car = WorkCar(30, "Grey", "Chevrolet Lacetti")
print(work_car.s, work_car.c, work_car.n,  work_car.i)
print(work_car.go(), work_car.turn('Налево'), work_car.show_speed(), work_car.stop())
police_car = PoliceCar(75,"While","Mercedes-AMG GLS 63")
print(police_car.s, police_car.c, police_car.n, police_car.i)
print(police_car.go())
print(police_car.turn("Направо"))
print(police_car.show_speed())
print(police_car.chase())
print(police_car.stop())

