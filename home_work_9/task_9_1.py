from time import perf_counter, sleep
from itertools import cycle

colors = {
    'Red': 7,
    'Yellow': 2,
    'Green': 3
}

sequence = ('Red', 'Yellow', 'Green')


class Color:
    def __init__(self, time, col=None):
        self._time = time
        self._nex_color = col


class TrafficLight:

    def __init__(self, col, sequence, color='Red'):
        it = cycle(sequence)
        next(it)
        self.__colors = {name: Color(time, next(it)) for name, time in col.items()}
        self.__color = color
        self._time_of_change = perf_counter()
        print(f'Color now is {color}')

    def running(self, color):
        color_now = self.__colors[self.__color]

        if color_now._nex_color != color.capitalize():
            raise Exception('Нарушена заданная последовательность')

        if perf_counter() - self._time_of_change < color_now._time:
            rem_time = color_now._time - (perf_counter() - self._time_of_change)
            print(f'Too fast, sleep for {rem_time} sec')
            sleep(rem_time)

        self.__color = color.capitalize()
        self._time_of_change = perf_counter()
        print(f'Color now is {self.__color}')


ex = TrafficLight(colors, sequence)
while True:
    ex.running('yellow')
    ex.running('green')
    ex.running('red')
