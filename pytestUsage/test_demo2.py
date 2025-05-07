import pytest


@pytest.mark.smoke
@pytest.mark.xfail
def test_demo_newprogram():
    greeting ="Hello"
    assert greeting == "Hi"


def test_demo_secondprogram_boards():
    a=10
    b=20
    assert a+10 == b

def test_crossbrowser(crossbrowser):
    print(crossbrowser)

def test_crossbrowse(crossbrowser1):
    print(crossbrowser1)