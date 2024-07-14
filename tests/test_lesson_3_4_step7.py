import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^ prepare_faces", "\n")
    yield
    print(":3 prepare_faces_end", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":) very_important_fixture", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р print_smiling_faces", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
        pass

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
        pass
