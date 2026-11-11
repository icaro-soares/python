class Employee:
    def __init__(self, name, last_name, salary=1_620):
        self.name = name.title()
        self.last_name = last_name.title()
        self.salary = salary


    def give_raise(self, value=5_000):
        self.salary += value
