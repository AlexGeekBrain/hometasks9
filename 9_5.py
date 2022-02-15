class Stationery:
    def __init__(self, title='чем-то'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


stat = Stationery()
pen = Pen('ручкой')
pencil = Pencil('карандашом')
handle = Handle('маркером')

office_supplies = [stat, pen, pencil, handle]

for i in office_supplies:
    i.draw()
