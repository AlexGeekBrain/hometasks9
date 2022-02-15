import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        while True:
            for key, val in self.__color.items():
                print(key)
                time.sleep(val)


tr_dict = {'\033[31m Red': 7, '\033[33m Yellow': 2, '\033[32m Green': 7}
a = TrafficLight(tr_dict)
a.running()

#________________________________________________________

# import time
# import itertools


# class TrafficLight:
#     __color = [['red', [7, 31]], ['yellow', [2, 33]], ['green', [7, 32]], ['yellow', [2, 33]]]

#     def running(self):
#         for light in itertools.cycle(self.__color):
#             print(f'\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m', end='')
#             time.sleep(light[1][0])


# a = TrafficLight()
# a.running()
