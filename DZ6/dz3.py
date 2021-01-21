#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу
# примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, wage, bonus):
        self.n = name
        self.s = surname
        self._i = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, wage, bonus):
        super().__init__(name, surname, wage, bonus)

    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.n + ' ' + self.s}")

    def get_total_income(self):
        print(f"Доход данного сотрудника с учетом премии {self._i['wage'] + self._i['bonus']} рублей.")



i = 1
while i <= 10:
    worker = Position(input('Введите имя сотрудника: '), input('Введите фамилию сотрудника: '), int(input("Введите оклад сотрудника: ")), int(input("Введите премию сотрудника: ")))
    i += 1
    worker.get_full_name()
    worker.get_total_income()
# или
#worker1 = Position(input('Введите имя сотрудника: '), 'Симаков', 50000, 20000)
#worker1.get_full_name()
#worker1.get_total_income()
#worker2 = Position('Марина', 'Снежина', 45000, 22000)
#worker2.get_full_name()
#worker2.get_total_income()