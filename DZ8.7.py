#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
#перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
#(комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного
#результата.
#1)
class ComplexNumber:

    def __init__(self, a, b):
        self.z_1 = complex(a, b)
        self.z_2 = complex(a, b)
        #print(self.z_1)
        #print(self.z_2)

                                    # z_1 и z_2 равны.
    def __add__(self, other):
        return f"Сложение комплексных чисел {self.z_1 + other.z_1}"

    def __mul__(self, other):
        return f"Умножение комплексных чисел {self.z_1 * other.z_1}"


com_num1 = ComplexNumber(1, 3)
com_num2 = ComplexNumber(-3, 9)
print(com_num1 + com_num2)
print(com_num1 * com_num2)
#a = 1 + 3j
#b = -3 + 9j
#print(a + b)
#print(a * b)




