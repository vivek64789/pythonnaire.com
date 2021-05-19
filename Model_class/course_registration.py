class CourseRegistration:
    """This class is model class to get values from Course registration form and
    set all data to the backend database table named courses"""

    def __init__(self, name, duration, credit, reg_date):
        self.__name = name
        self.__duration = duration
        self.__credit = credit
        self.__reg_date = reg_date

    # ===========================set methods=======================

    def set_name(self, name):
        self.__name = name

    def set_duration(self,duration):
        self.__duration = duration

    def set_credit(self,credit):
        self.__credit=credit

    # =====================get methods========================

    def get_name(self):
        return self.__name

    def get_duration(self):
        return self.__duration

    def get_credit(self):
        return self.__credit

    def get_reg_date(self):
        return self.__reg_date


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
