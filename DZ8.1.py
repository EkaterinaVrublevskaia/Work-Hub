#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
#«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
#месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
#числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day_mouth_year):
        #self.d = day
        #self.m = mouth
        #self.y = year
        self.day_mouth_year = day_mouth_year


    @classmethod
    def s_method(cls, day_mouth_year):    # сделать это по другому
        #date = list(day_mouth_year.split('.'))
        date = []
        for en in day_mouth_year.split():
            if en != '.':
                date.append(en)
        return date

    @staticmethod
    def met_valid(day, mouth, year):
        if 0 != day <= 31 and 0 != mouth <= 12 and 0 != year <= 3333:
            return f"Все верно!"
        else:
            return f"Ошибка при вводе данных!"


#t = input("Введите сегодняшний день.месяц.год через точку: ")
today = Date('22.1.2021')
print(today.met_valid(32, 10, 2020))
print(Date.met_valid(21, 0, 2020))
print(today.met_valid(21, 10, -1))
print(Date.met_valid(21, 11, 2020))
print(today.s_method('21.11.2020'))
print(Date.s_method('21.11.2020'))
print(today.day_mouth_year)


