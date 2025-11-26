class Employee:
    def __init__(self, employee_id=None, first_name=None, last_name=None, email=None,
                 phone_number=None, job_title=None, age=None):
        self._employee_id = employee_id          # None when creating a new employee
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number
        self._job_title = job_title
        self._age = age

    def __str__(self):
        return (f"Employee[ID: {self._employee_id}, "
                f"Name: {self._first_name} {self._last_name}, "
                f"Email: {self._email}, Phone: {self._phone_number}, "
                f"Job Title: {self._job_title}, Age: {self._age}]")

    # -------- Properties --------
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, value):
        self._job_title = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    # -------- Utility --------
    def to_dict(self):
        return {
            "employee_id": self._employee_id,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "email": self._email,
            "phone_number": self._phone_number,
            "job_title": self._job_title,
            "age": self._age
        }


class Department:
    def __init__(self, department_id=None, department_name=None, location=None, manager_id=None):
        self._department_id = department_id
        self._department_name = department_name
        self._location = location
        self._manager_id = manager_id

    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value

    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def manager_id(self):
        return self._manager_id

    @manager_id.setter
    def manager_id(self, value):
        self._manager_id = value


class Salaries:
    def __init__(self, salary_id=None, employee_id=None, amount=None, effective_date=None):
        self._salary_id = salary_id
        self._employee_id = employee_id
        self._amount = amount
        self._effective_date = effective_date

    @property
    def salary_id(self):
        return self._salary_id

    @salary_id.setter
    def salary_id(self, value):
        self._salary_id = value

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
