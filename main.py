import pytest
import unittest
from TestCases.LoginPage_test import LoginTest

LoginPageTest = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
BasicTest = unittest.TestSuite([LoginPageTest])
unittest.TextTestRunner(verbosity=1).run(BasicTest)