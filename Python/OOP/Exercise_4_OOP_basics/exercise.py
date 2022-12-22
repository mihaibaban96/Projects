import time
import random
import os


class Company:
    TYPE = "Corporation"
    companies = []

    def __init__(self, name, address, number_of_maximum_employees, field, date_founded, fiscal_value_per_year):
        self.name = name
        self.address = address
        self.number_of_maximum_employees = number_of_maximum_employees
        self.field = field
        self.date_founded = date_founded
        self.employees = []
        self.company_shares = 100
        self.fiscal_value_per_year = fiscal_value_per_year
        Company.companies.append(self)

    def sell_shares(self, percent_of_shares, shares_price):
        if self.company_shares > percent_of_shares:
            print(
                f"{self.name} is selling {percent_of_shares}% actions from company.....")
            self.company_shares -= percent_of_shares
            self.fiscal_value_per_year += shares_price
            print(
                f"Remaining shares: {self.company_shares}%.\n Current fiscal value for this year: {self.fiscal_value_per_year}")
        else:
            print("Company doesn't have enough shares to sell....")

    def calculate_profit(self, applicable_taxes):
        profit = self.fiscal_value_per_year - \
            ((applicable_taxes/100) * self.fiscal_value_per_year)
        print(f"Profit for this year: {profit}$")
        return profit

    def add_employees(self, empl):
        if len(self.employees) < self.number_of_maximum_employees:
            self.employees.append(empl)
            print(f"Employee {empl.name} is now part of our company!")
            print(f"Current employees: {self.employees}\n")
        else:
            return "Maximum number of employees reached!"

    def show_employees(self):
        for empl in self.employees:
            print(f"employee: {empl} name: {empl.name}")

    def show(self):
        print('''With headquarters in {self.address}, {self.name} provides superior services.\n
        Founded in {self.date}, {self.name} delivers the best  services in the field of {self.field}.\n
        Our motto is always to deliver the best and satisfy the clients! 
        ''')

    def sell_itself(self):
        print("Sometimes companies choose to retreat from the market.....\n ")
        print(f"{self.name} located in {self.address} choosed to end it's bussiness and to leave the market\n")
        Company.companies = list(
            filter(lambda x: x != self, Company.companies))
        return Company.companies

    @classmethod
    def show_companies(cls):
        for comp in cls.companies:
            print(f"{comp.name} {comp.address}")

    def __str__(self):
        return f"Company {self.name}.\n Headquarters: {self.address}"


class Employee:
    def __init__(self, name, phone_number, address, salary, function, seniority, work_place, can_own_shares):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.salary = salary
        self.function = function
        self.seniority = seniority
        self.work_place = work_place
        self.can_own_shares = can_own_shares

    def show(self):
        return f"Hello! I am {self.name} and I have a seniority of {self.seniority} years at {self.work_place}. My speciality is {self.function} \n."

    def tell_sallary(self):
        return f"Hello! My salary is {self.salary}$ per month.... It's not much... But it's honest work...\n"

    def calculate_seniority(self):
        if self.seniority > 10:
            return "Expert"
        elif self.seniority > 5:
            return "Senior "
        elif self.seniority > 3:
            return "Mid"
        elif self.seniority > 1:
            return "Junior"
        else:
            return "Intern..."

    def buy_shares(self):
        if self.can_own_shares:
            print("Now I am am buying some shares! Great! I just increased my shares")
        else:
            print("I can not buy shares")

    def __str__(self):
        return f"Employee: {self.name} with address {self.address} working at {self.work_place.name}"


class ChiefExecutiveOfficer(Employee):
    def __init__(self, name, phone_number, address, salary, function, seniority, work_place, can_own_shares):
        super().__init__(name, phone_number, address, salary,
                         function, seniority, work_place, can_own_shares)

    def fire_someone(self, employee):
        print(
            f"Employee: {employee.name} working at {employee.work_place.name} was fired!!")
        employee.work_place.employees = list(
            filter(lambda x: x != employee, employee.work_place.employees))
        return f"Current employees at {employee.work_place.name} : {employee.work_place.employees} \n"


class HumanResources(Employee):
    def __init__(self, name, phone_number, address, salary, function, seniority, work_place, can_own_shares):
        super().__init__(name, phone_number, address, salary,
                         function, seniority, work_place, can_own_shares)

    def hire_somebody(self, employee):
        print(f"Employee {employee.name} was just hired")
        print(
            f"He is a great {employee.function} and starting from today he will be our new colleague!")
        employee.work_place.employees.append(employee)
        return f"Current employees at {employee.work_place.name} : {employee.work_place.employees}"


class SoftwareEngineer(Employee):
    def __init__(self, name, phone_number, address, salary, function, seniority, work_place, can_own_shares, technologies):
        super().__init__(name, phone_number, address, salary,
                         function, seniority, work_place, can_own_shares)
        self.technologies = technologies

    def create_an_app(self):
        print(
            f"I just created an app in {self.technologies}\n Now my salary will be raised!")
        self.salary += 1000

    def do_task(self, task):
        t = random.randint(0, 7)
        dt = t
        while t > 0:
            time.sleep(1)
            t -= 1
            print("Still working at task ..../...")
            time.sleep(0.5)
            os.system('cls')

        print(f"Done! I finished doing this task in {dt} weeks!")


company_1 = Company("Endava", "London, Great Britain", 5000,
                    "Software Engineering", "1996-12-20", 100)
company_3 = Company("NTT DATA", "Bucharest, Romamia", 5000,
                    "Software Engineering", "1996-12-20", 100)
company_2 = Company("Endava", "Brusseless, Belgium", 5000,
                    "Software Engineering", "1996-12-20", 100)
empl1 = Employee("John Doe", "+40 770 696 893", "Central Boulevard, no1, London",
                 3000, "Software Engineer", 5, company_1, False)
empl2 = Employee("Mark Walhberg", "+40 770 696 873", "Central Boulevard, no2, London",
                 3000, "Software Engineer", 5, company_1, False)
ceo1 = ChiefExecutiveOfficer("Bill Gates", "+40 770 567 889",
                             "Sillicon Valley, USA", 10000, "CEO", 30, company_3, True)
hr1 = HumanResources("Alana Rey", "+40 777 567 889",
                     "Central London, GB", 500, "Human Resources", 3, company_1, False)
soft_1 = SoftwareEngineer("Zukerbergul", "+40 770 696 893", "Central Boulevard, no1, London",
                          3000, "Software Engineer", 10, company_1, False, "Python/Django/React")

soft_1.create_an_app()
soft_1.do_task("Create a web app in Django")
