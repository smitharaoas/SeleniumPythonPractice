import pytest


@pytest.fixture(scope="class")

def startup():
    print("Initial Setup done")
    yield
    print("Test execution completed")


@pytest.fixture()
def dataload():
    print("User profile data from fixture")
    return["Smitha","Rao","Female"]

@pytest.fixture(params=["Chrome","Firefox","IE"])
def crossbrowser(request):
    return request.param

@pytest.fixture(params=[("Chrome","Smitha"),("Firefox","Ahsok"),("IE","Thejas")])
def crossbrowser1(request):
    return request.param