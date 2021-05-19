class EmployeeRegistration:
    """This class is model class to get values from Employee registration form and
    set all data to the backend database table named Employees"""

    def __init__(self, username, email, password, f_name, l_name, dob, gender, address, contact, job, reg_as,
                 qualification, department, reg_date):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__f_name = f_name
        self.__l_name = l_name
        self.__dob = dob
        self.__gender = gender
        self.__address = address
        self.__contact = contact
        self.__job = job
        self.__reg_as=reg_as
        self.__qualification=qualification
        self.__department=department
        self.__reg_date = reg_date

    # ===========================set methods=======================

    def set_username(self, username):
        self.__username = username

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_f_name(self, f_name):
        self.__f_name = f_name

    def set_l_name(self, l_name):
        self.__l_name = l_name

    def set_dob(self, dob):
        self.__dob = dob

    def set_gender(self, gender):
        self.__gender = gender

    def set_address(self, address):
        self.__address = address

    def set_contact(self, contact):
        self.__contact = contact

    def set_job(self, job):
        self.__job = job

    def set_reg_as(self, reg_as):
        self.__reg_as = reg_as

    def set_qualification(self, qualification):
        self.__qualification = qualification

    def set_department(self, department):
        self.__department = department

    def set_reg_date(self, reg_date):
        self.__reg_date = reg_date

    # =====================get methods========================

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_f_name(self):
        return self.__f_name

    def get_l_name(self):
        return self.__l_name

    def get_dob(self):
        return self.__dob

    def get_gender(self):
        return self.__gender

    def get_address(self):
        return self.__address

    def get_contact(self):
        return self.__contact

    def get_job(self):
        return self.__job

    def get_reg_as(self):
        return self.__reg_as

    def get_qualification(self):
        return self.__qualification

    def get_department(self):
        return self.__department

    def get_reg_date(self):
        return self.__reg_date


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
