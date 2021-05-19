import mysql.connector
import os
import pickle


class DatabaseConnection:
    """connect front end to database, here all the backend code are written, such as insert,
    update, delete, select"""

    def __init__(self):
        # Frontend.connect_database.SaveDatabaseHost()
        self.file()

    def file(self):
        """Unpickle the files and extract the host credentials such as
        host, port, username, password which are then used to connect to the database"""

        self.len = os.path.getsize("D:\\Softwarica study material\\Semester 2\\Introduction to Algorithm\\Coding_and_"
                                   "Algorithms\\190352_Bibekanand_kushwaha_Sem_2_Final_assignment\\Frontend\\"
                                   "database_data.txt")
        if self.len > 0:
            f = open("D:\\Softwarica study material\\Semester 2\\Introduction to Algorithm\\Coding_and_"
                     "Algorithms\\190352_Bibekanand_kushwaha_Sem_2_Final_assignment\\Frontend\\"
                     "database_data.txt", "rb")
            self.dictcred = pickle.load(f)

            for k, p in self.dictcred.items():
                l = p[0]
                po = p[1]
                u = p[2]
                pa = p[3]
                self.d_connection(l, po, u, pa)

    def d_connection(self, host, port, username, password):
        """takes 4 functional arguments host is the domain of server, port is where the proxy server is forwarding,
        username is the username of host and password is that password used while setting up user"""
        self.connection = mysql.connector.connect(host=host, port=port, user=username, password=password)
        self.cursor = self.connection.cursor()

    def __del__(self):
        """if connection is found without usage then this will anyhow close that connection"""
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()

        except BaseException as msg:
            pass

    def create(self, query):
        """ used to create the database in the host"""
        self.cursor.execute(query)
        self.connection.commit()

    def search(self, query, values):
        """ search the values from database"""
        self.cursor.execute(query, values)
        data = self.cursor.fetchall()
        self.connection.commit()
        return data

    def insert(self, query, values):
        """ insert values from frontend to database"""
        self.cursor.execute(query, values)
        self.connection.commit()

    def select(self, query):
        """:returns data """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.connection.commit()
        return data

    def update(self, query, values):
        """updates the values from frontend"""
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete(self, query, values):
        """ deletes the data from database"""
        self.cursor.execute(query, values)
        self.connection.commit()


DatabaseConnection()
