import pytest


@pytest.mark.usefixtures("dataload")

class TestDataDriven:
    def test_datadriven(self,dataload):
        print(dataload)
