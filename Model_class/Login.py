class Login:
    """this is the model class for Login class from module login_form, it connects frontend and
        backend """
    def __init__(self, id_, username, email, password):
        self.__id_ = id_
        self.__username = username
        self.__email = email
        self.__password = password

    # set values
    def set_id(self, id_):
        self.__id_ = id_

    def set_username(self, username):
        self.__username = username

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    # get values
    def get_id(self):
        return self.__id_

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password
