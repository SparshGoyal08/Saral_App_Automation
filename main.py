import pytest


def suite():
    pytest.main(["-s", "TestCases/LoginPage_test.py"])


if __name__ == "__main__":
    suite()
