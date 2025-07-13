class Company:
    def __init__(self, name, contact):
        self._name = name
        self._contact = contact
        self._employee_list = []

    def subscribe(self, employee):
        if employee not in self._employee_list:
            self._employee_list.append(employee)
            print(f"{employee.name} subscribed to company updates.")
        else:
            print(f"{employee.name} is already subscribed.")

    def update(self, new_name):
        print(f"\nUpdating company name from '{self._name}' to '{new_name}'")
        self._name = new_name
        self._notify()

    def _notify(self):
        print("Notifying employees...")
        for employee in self._employee_list:
            employee.update(self._name)

    @property
    def name(self):
        return self._name

    @property
    def contact(self):
        return self._contact


class Employee:
    def __init__(self, name, company_name):
        self.name = name
        self.company_name = company_name

    def update(self, new_company_name):
        print(f"{self.name}: Company name updated to '{new_company_name}'")
        self.company_name = new_company_name


# Example usage
company = Company("Tricon", "13")

emp1 = Employee("Prabhu", "Tricon")
emp2 = Employee("Pra", "Tricon")

company.subscribe(emp1)
company.subscribe(emp2)

company.update("HCL")
