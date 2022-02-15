class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}, {self.position}:')

    def get_total_income(self):
        salary = 0
        for key, val in self._income.items():
            salary += val
            print(f'{key}: {val} rub')
        print(f'total: {salary} rub')


a = Position('Ivan', 'Ivanov', 'engineer', {'wage': 100000, 'bonus': 50000})
a.get_full_name()
a.get_total_income()
