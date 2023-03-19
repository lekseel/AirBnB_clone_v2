import MySQLdb
import os
import unittest

class TestStates(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up a connection to the test database
        cls.db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST', 'localhost'),
            user=os.getenv('HBNB_MYSQL_USER', 'root'),
            passwd=os.getenv('HBNB_MYSQL_PWD', ''),
            db=os.getenv('HBNB_MYSQL_DB', 'hbnb_test_db'),
            port=3306
        )
        # Create a cursor for executing queries
        cls.cur = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        # Close the database connection
        cls.db.close()

    def setUp(self):
        # Get the initial number of records in the states table
        self.cur.execute('SELECT COUNT(*) FROM states')
        self.initial_count = self.cur.fetchone()[0]

    def tearDown(self):
        # Roll back any changes made during the test
        self.db.rollback()

    def test_create_state(self):
        # Execute the console command to create a new state
        os.system('echo "create State name=\'California\'" | ./console.py')

        # Get the new number of records in the states table
        self.cur.execute('SELECT COUNT(*) FROM states')
        new_count = self.cur.fetchone()[0]

        # Check that the new count is one greater than the initial count
        self.assertEqual(new_count, self.initial_count + 1)
