class DatabaseConnected:
    """ This class is used to connect frond end and backend when Database
    is successfully created"""
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    # set methods

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    # get methods

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database


class AdminData:
    """ This class is used to connect frond end and backend for Admin Data"""
    def __init__(self, username,email, password):
        self.__email = email
        self.__username = username
        self.__password = password

    # set methods

    def set_username(self, username):
        self.__username = username

    def set_email(self,email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    # get methods

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

