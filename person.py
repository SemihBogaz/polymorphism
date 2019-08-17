class Person:

    def __init__(self, name: str, surname: str, citizen_id: int):
        self.Name = name
        self.Sname = surname
        self.ID = citizen_id


class Unemployed(Person):
    pass


class Employed(Person):

    def __init__(self, name: str, surname: str, citizen_id: int, idno: int, salary: float):
        Person.__init__(self, name, surname, citizen_id)
        self.ID_NO = idno
        self.Salary = salary

    def raise_on_salary(self, amount: float):
        self.Salary += amount


class Engineer(Employed):

    def __init__(self, name: str, surname: str, citizen_id: int, idno: int, salary: float, prog_lang: tuple, foreign_lang: tuple, office_prog:tuple ):
        Employed.__init__(self, name, surname, citizen_id, idno, salary)
        self.Prog_Lang = prog_lang
        self.Foreign_Lang = foreign_lang
        self.Office_prog = office_prog


class Accountant(Employed):

    def __init__(self, name: str, surname: str, citizen_id: int, idno: int, salary: float, office_prog: tuple):
        Employed.__init__(self, name, surname, citizen_id, idno, salary)
        self.Office_prog = office_prog


x = Engineer("Semih", "Boğaz", 1234, 1, 1000, ("java", "python "), ("English", "German"), ("MS office",))
y = Accountant("Asdg", "Zxvb", 5667, 2, 800, ("MS office",))

print(x.Foreign_Lang)
print(y.Office_prog)
print(x.Salary)
x.raise_on_salary(20)
print(x.Salary)






