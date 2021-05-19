class StudentRegistration:
    """This class is model class to get values from Student registration form and
    set all data to the backend database table named students"""

    def __init__(self, username, email, password, f_name, l_name, dob, gender, address, contact, shift, course_id,
                 batch_id, section, reg_date):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__f_name = f_name
        self.__l_name = l_name
        self.__dob = dob
        self.__gender = gender
        self.__address = address
        self.__contact = contact
        self.__shift = shift
        self.__course_id = course_id
        self.__batch_id = batch_id
        self.__section = section
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

    def set_shift(self, shift):
        self.__shift = shift

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def set_batch_id(self, batch_id):
        self.__batch_id = batch_id

    def set_section(self, section):
        self.__section = section

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

    def get_shift(self):
        return self.__shift

    def get_course_id(self):
        return self.__course_id

    def get_batch_id(self):
        return self.__batch_id

    def get_section(self):
        return self.__section

    def get_reg_date(self):
        return self.__reg_date


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
