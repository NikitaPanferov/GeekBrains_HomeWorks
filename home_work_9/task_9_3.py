class Worker:

    def __init__(self, name, surname, position, income, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': income, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname.capitalize()} {self.name.capitalize()}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker1 = Position('nikita', 'panferov', 'Boss', 100, 50)
print(worker1.get_full_name(), worker1.get_total_income())