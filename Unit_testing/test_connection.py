import unittest
from Backend.connection import DatabaseConnection


class TestConnection(unittest.TestCase):
    def setUp(self):
        self.db_obj = DatabaseConnection()
        self.db_con = self.db_obj.d_connection('localhost', '3306', 'root', '')
        self.values = (1, 'vivek', 'vivek@gmail.com')

    def test_create(self):
        query = "create database test_cms"
        actual = self.db_obj.create(query)
        self.assertIsNone(actual)

    # def test_use(self):
    #     query1 = "use test_cms"
    #     actual1 = self.db_obj.create(query1)
    #     self.assertIsNone(actual1)

    def test_create_table(self):
        query1 = "use test_cms"
        actual1 = self.db_obj.create(query1)
        self.assertIsNone(actual1)

        query2 = "create table test_student(test_id int NOT NULL," \
                 "test_name VARCHAR (50), test_email VARCHAR (50), CONSTRAINT PK_test_id PRIMARY KEY (test_id))"

        actual2 = self.db_obj.create(query2)
        self.assertIsNone(actual2)

    def test_insert(self):
        query = "use test_cms"
        actual = self.db_obj.create(query)
        self.assertIsNone(actual)

        query1 = "insert into test_student (test_id, test_name, test_email)values (%s, %s, %s)"
        self.db_obj.insert(query1, self.values)

        query2 = "select * from test_student where test_id = 1"
        # values = (1,)
        actual = self.db_obj.select(query2)
        expected1 = [(1, 'vivek', 'vivek@gmail.com'), ]
        self.assertEqual(expected1, actual)

    def test_delete(self):
        query = "use test_cms"
        actual = self.db_obj.create(query)
        self.assertIsNone(actual)

        query1 = "delete from test_student where test_id=%s"
        values = (1,)
        self.db_obj.delete(query1, values)
        query2 = "select * from test_student where test_id = %s"
        values = (1,)
        actual = self.db_obj.search(query2, values)
        expected1 = []
        self.assertEqual(expected1, actual)

    def test_select(self):
        query = "drop database test_cms"
        actual = self.db_obj.create(query)
        self.assertIsNone(actual)