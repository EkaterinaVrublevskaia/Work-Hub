#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора
# в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав
# экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
#1)
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

class TrafficLight:
    #__color = [Fore.RED + 'Красный', Fore.YELLOW + 'Желтый', Fore.GREEN + 'Зеленый'] #1
    __color = ['Красный', 'Желтый', 'Зеленый'] #2
    def runnung(self):
        # try:
        count = 0
        while count < 3:
            #print(f'Светофор переключается на {self.__color[count]}') #1
            if count == 0:
                print(Fore.RED + f'Светофор переключается на {self.__color[count]}') #2
                time.sleep(7)
            elif count == 1:
                print(Fore.YELLOW + f'Светофор переключается на {self.__color[count]}')
                time.sleep(2)
            elif count == 2:
                print(Fore.GREEN + f'Светофор переключается на {self.__color[count]}')
                time.sleep(7)
        #except: # вместо else:
            else:
                print(f"404Error")
            count += 1


trafficLight = TrafficLight()
#trafficLight.runnung()
# or
try:
    trafficLight.runnung()
except:
    print(f"404Error")

#2) or
#class TrafficLight:
#    __color = [Fore.RED + 'Красный', Fore.YELLOW + 'Желтый', Fore.GREEN + 'Зеленый']
#
#    def runnung(self):
#        try:
#            count = 0
#            while count < 3:
#                print(f'Светофор переключается на {self.__color[count]}')
#                count += 1
#        except:
#            print(f"404Error")

#trafficLight = TrafficLight()
#trafficLight.runnung()