#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
#который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
#уникальные для каждого типа оргтехники.
#5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
#определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
#данных, можно использовать любую подходящую структуру, например словарь.
#6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
#для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
#на уроках по ООП.

class OfficeEquipmentWarehouse:
    def __init__(self):
        self.dict = {}

    def add(self, equipment):
        self.dict.setdefault(equipment.group_name(), []).append(equipment)


class OfficeEquipment:

    def __init__(self, name, price, quantity):
        self.n = name
        self.pr = price
        self.q = quantity
        self.s = price * quantity
        self.list = 50
        self.my_table = []
        self.gr_n = self.__class__.__name__

    def group_name(self):
        return f"{self.gr_n}"

    def __repr__(self):
        return f"{self.n}  {self.pr}  {self.q}  {self.s }"

    def __str__(self):
        return f"Добавляем на склад: \n   'Название устройства': {self.n}\n   'Цена': {self.pr}\n   'Количество': {self.q}\n   'Общая стоимость': {self.s}"

    def func(self):
        print(f"Данная машина печатает {self.list} листов.")

    # общее, не сделано чтобы выводило в склад по отдельности.
    def additions_table(self):
        while True:
            try:
                name = input('Введите название техники: ')
                price = int(input('Введите цену за ед.: '))
                quantity = int(input('Введите количество: '))
                new_my_d = {'Название устройства': name, 'Цена за ед. ': price, 'Количество': quantity,
                            'Общая стоимость': price * quantity}
                self.my_table.append(new_my_d)
                end = input("Для выхода введите 'Q', для того чтобы продолжить - 'Enter'")
                if end == 'Q' or end == 'q':
                    break
                else:
                    continue
            except:
                return f"Ошибка ввода данных! Будьте внимательны!"
        print(f"Список на текущий момент - \n {self.my_table}")
        #features = {'Модель': '', 'цена': '', 'количество': ''}
        #analytics = {'Модель': [], 'цена': [], 'количество': []}
        #i = 0
        #while True:
        #    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        #        break
        #    i += 1
        #    for f in features.keys():
        #        pro = input(f'Введите "{f}": ')
        #        features[f] = int(pro) if f == 'цена' or f == 'количество' else pro
        #        analytics[f].append(features[f])
        #    self.my_table.append((i, features))
        #    print(f'\nСтруктура товаров\n{self.my_table}')
        #    print(f'\nТекущая аналитика по товарам: \n {"*" * 30}')
        #    for key, value in analytics.items():
        #       print(f'{key[:25]:>30}: {value}')
        #    print('*' * 30)


class Printer(OfficeEquipment):
    def __init__(self, name, price, quantity, color):
        super().__init__(name, price, quantity)
        self.s = price * quantity
        self.c = color

    def func(self):
        return f"Принтер печатает {self.list} листов. {self.c}."


class Scanner(OfficeEquipment):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.s = price * quantity

    def func(self):
        return f"Сканер сканирует {self.list} фотографий."


class Xerox(Printer, Scanner):
    def __init__(self, name, price, quantity, color):
        super().__init__(name, price, quantity, color)
        self.s = price * quantity
        #self.monochrome = 'в - монохром'

    def func(self):
        return f"Ксерокс копирует {self.list} листов {self.c}."


sklad = OfficeEquipmentWarehouse()
printer = Printer('HP LaserJet', 7690, 3, 'Печать - цветная')
print(printer.__str__())
print(printer.func())
scanner = Scanner('Canon CanoScan LiDE 300', 5150, 2)
print(scanner.__str__())
print(scanner.func())
xerox = Xerox('Xerox WorkCentre 3025BI', 11930, 1, 'в ч\б цвете')
print(xerox.__str__())
print(xerox.func())
sklad.add(printer)
sklad.add(scanner)
sklad.add(xerox)
print(sklad.dict)
print("Введите информацию по принтерам!")
printer.additions_table()
#scanner.additions_table()
#xerox.additions_table()




