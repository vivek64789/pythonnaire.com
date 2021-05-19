class SectionRegistration:
    """This class is model class to get values from section registration form and
    set all data to the backend database table named section"""

    def __init__(self, code, name, capacity, reg_date):
        self.__code = code
        self.__name = name
        self.__capacity = capacity
        self.__reg_date = reg_date

    # ===========================set methods=======================

    def set_code(self, code):
        self.__code = code

    def set_name(self, name):
        self.__name = name

    def set_capacity(self, capacity):
        self.__capacity=capacity

    def set_reg_date(self, reg_date):
        self.__reg_date = reg_date

    # =====================get methods========================

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def get_capacity(self):
        return self.__capacity

    def get_reg_date(self):
        return self.__reg_date


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
