class Employee:
  def __init__(self,employee_id, first_name, last_name, email, phone_number, job_title, age ):
    self.__employee_id = employee_id
    self._first_name = first_name
    self._last_name = last_name
    self._email = email
    self._phone_number = phone_number
    self._job_title = job_title
    self._age = age

  def __str__(self):
    return f"Employee[ID: {self.__employee_id}, Name: {self._first_name} {self._last_name}, Email: {self._email}, Phone: {self._phone_number}, Job Title: {self._job_title}, age: {self._age}]"
  
  @property
  def get_employee_id(self):
      return self.__employee_id

  @property
  def get_first_name(self):
      return self._first_name

  @property
  def get_last_name(self):
      return self._last_name

  @property
  def get_email(self):
      return self._email

  @property
  def get_phone_number(self):
      return self._phone_number

  @property
  def get_job_title(self):
      return self._job_title
  
  @property
  def get_age(self):
      return self._age

  @get_employee_id.setter
  def update_employee_id(self, new_id):
      self.__employee_id = new_id
  
  @get_first_name.setter
  def update_first_name(self, new_name):
      self._first_name = new_name
  
  @get_last_name.setter
  def update_last_name(self, new_name):
      self._last_name = new_name
  

  @get_email.setter
  def update_email(self, new_email):
      self._email = new_email

  @get_phone_number.setter
  def update_phone_number(self, new_phone):
      self._phone_number = new_phone

  @get_job_title.setter
  def update_job_title(self, new_title):
      self._job_title = new_title

  @get_age.setter
  def update_age(self, new_age):
      self._age = new_age
  
  
  def to_dict(self):
      return {
          "employee_id": self.__employee_id,
          "first_name": self._first_name,
          "last_name": self._last_name,
          "email": self._email,
          "phone_number": self._phone_number,
          "job_title": self._job_title
      }


class Department:
    def __init__(self,department_id, department_name, location, manager_id,):
        self._department_id = department_id
        self._department_name = department_name
        self._location = location
        self._manager_id = manager_id

    @property
    def get_department_id(self):
        return self._department_id
    
    @property
    def get_department_name(self):
        return self._department_name
    
    @property
    def get_location(self):
        return self._location
    
    @property
    def get_manager_id(self):
        return self._manager_id
    
    @get_department_id.setter
    def update_department_id(self, new_department_id):
        self._department_id = new_department_id

    @get_department_name.setter
    def update_department_name(self, new_department_name):
        self._department_name = new_department_name

    @get_location.setter
    def update_location(self, new_location):
        self._location = new_location

    @get_manager_id.setter
    def update_manager_id(self, new_manager_id):
        self._manager_id = new_manager_id


class Salaries:
    def __init__(self, salary_id, employee_id, amount, effective_date):
        self._salary_id = salary_id
        self._employee_id = employee_id
        self._amount = amount
        self._effective_date = effective_date

    @property
    def get_salary_id(self):
        return self._salary_id

    @property
    def get_employee_id(self):
        return self._employee_id

    @property
    def get_amount(self):
        return self._amount

    @property
    def get_effective_date(self):
        return self._effective_date

    @get_salary_id.setter
    def update_salary_id(self, new_salary_id):
        self._salary_id = new_salary_id

    @get_employee_id.setter
    def update_employee_id(self, new_employee_id):
        self._employee_id = new_employee_id

    @get_amount.setter
    def update_amount(self, new_amount):
        self._amount = new_amount

    @get_effective_date.setter
    def update_effective_date(self, new_effective_date):
        self._effective_date = new_effective_date
