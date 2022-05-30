# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.


from time import sleep


class TrafficLight():
    def __init__(self, color):
        self._color = color

    def running(self):
        color_pause = {'Green': 8, 'Yelow': 2, 'Red': 5}
        if self._color not in color_pause.keys():
            raise ValueError('Неверный цвет')

        else:
            color_list = [key for key in color_pause.keys()]
            start = color_list.index(self._color)
            while True:
                if start == len(color_list):
                    start = 0
                else:
                    print(color_list[start])
                    sleep(color_pause[color_list[start]])
                    start += 1




my_tl = TrafficLight('Brown')
my_tl.running()



my_trafickligth = TrafficLight('Green')
my_trafickligth.running()
