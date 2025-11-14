class Employees:
  def __init__(self,employee_id, first_name, last_name, email, phone_number, job_title):
    self.__employee_id = employee_id
    self._first_name = first_name
    self._last_name = last_name
    self._email = email
    self._phone_number = phone_number
    self._job_title = job_title

  def __str__(self):
    return f"Employee[ID: {self.__employee_id}, Name: {self._first_name} {self._last_name}, Email: {self._email}, Phone: {self._phone_number}, Job Title: {self._job_title}]"
  
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
  
  def to_dict(self):
      return {
          "employee_id": self.__employee_id,
          "first_name": self._first_name,
          "last_name": self._last_name,
          "email": self._email,
          "phone_number": self._phone_number,
          "job_title": self._job_title
      }
  
