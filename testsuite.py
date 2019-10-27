import unittest
import tests.test_employee
import tests.test_restaurant
import tests.test_menu
from extras.database import Database


loader = unittest.TestLoader()
suite = unittest.TestSuite()

database = Database()
database.recreate_tables()

suite.addTests(loader.loadTestsFromModule(tests.test_employee))
suite.addTests(loader.loadTestsFromModule(tests.test_restaurant))
suite.addTests(loader.loadTestsFromModule(tests.test_menu))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
