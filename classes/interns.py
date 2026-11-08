from .employees import Employee


class Intern(Employee):
    def __init__(self, name, salary, months):
        if 1 > months > 12:
            raise ValueError("months must be 1-12")
        super().__init__(name, salary)
        self.months = months


    def title(self):
        return "Intern"


    