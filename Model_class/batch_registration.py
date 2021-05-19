class BatchRegistration:
    """This class is model class to get values from Batch registration form and
    set all data to the backend database table named Batch"""

    def __init__(self, name, year, intake, reg_date):
        self.__name = name
        self.__year = year
        self.__intake = intake
        self.__reg_date = reg_date

    # ===========================set methods=======================

    def set_name(self, name):
        self.__name = name

    def set_year(self, year):
        self.__year = year

    def set_intake(self, intake):
        self.__intake = intake

    def set_reg_date(self, reg_date):
        self.__reg_date = reg_date

    # =====================get methods========================

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_intake(self):
        return self.__intake

    def get_reg_date(self):
        return self.__reg_date


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
