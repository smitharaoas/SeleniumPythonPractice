import pytest

@pytest.mark.usefixtures("startup")

class TestNewDemo:
    def test_programme(self):
        print("Hello")

    def test_newp1_boards(self):
        print("Using fixture1!")

    def test_newp2_boards(self):
        print("Using fixture2!")

    def test_newp3_boards(self):
        print("Using fixture3!")

    def test_newp4_boards(self):
        print("Using fixture4!")