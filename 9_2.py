class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_profit(self, weight=25, thickness=5):
        print(f'{(self._length * self._width * weight * thickness) / 1000} т.')


a = Road(5000, 20)
a.calc_profit()
