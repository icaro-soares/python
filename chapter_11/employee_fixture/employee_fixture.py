class Employee:
    def __init__(self, first_name, last_name, salary=1_621):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


    def give_raise(self, value=10_000):
        self.salary += value
