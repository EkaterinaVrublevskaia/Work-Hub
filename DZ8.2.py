#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
#вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
#ситуацию и не завершиться с ошибкой.

class DivisionZero(Exception):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def division(a, b):
        try:
            return a / b or b / a
        except ZeroDivisionError:
            return f"Ошибка в делении. Проверите переменные."


d_z = DivisionZero(1000, 5)
print(d_z.division(50, 0))
print(DivisionZero.division(0, 55))
print(DivisionZero.division(11, -11))
print(d_z.division(50, 5.5))

#2 способ) не работает проверка
class DivisionZero(Exception):

    def __init__(self, txt):
        self.txt = txt


num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')

try:
    num1 = int(num1)
    num2 = int(num2)
    if num1 == 0 or num2 == 0:
        raise DivisionZero("Ошибка в делении на ноль!")
except ZeroDivisionError as err:
    print(err)
else:
    print(num1 / num2)
finally:
    print("Конец")





