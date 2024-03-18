from app.io.input import read_file, read_file_pandas
import pandas as pd


def test_read_file(tmp_path):
    file_test = tmp_path / "file_test.txt"
    file_test.write_text("something just to test this file")
    assert read_file(str(file_test)) == "something just to test this file"


def test_read_file_empty(tmp_path):
    test_file = tmp_path / "empty_file.txt"
    assert read_file(str(test_file)) == ""


def test_read_file_error_not_exist():
    assert read_file("we_dont_have_this_file.txt") is None


def test_read_file_pandas(tmp_path):
    test_content = "A,S,P\nAlbinos,Sobaka,Pes\nAlbina,Stepan,Patron\nAnanas,Slyva,Papaya"
    file_test = tmp_path / "file_test.txt"
    file_test.write_text(test_content)
    assert read_file_pandas(str(file_test)).equals(
        pd.DataFrame({"A": ["Albinos", "Albina", "Ananas"], "S": ["Sobaka", "Stepan", "Slyva"],
                      "P": ["Pes", "Patron", "Papaya"]})
    )


def test_read_file_pandas_empty(tmp_path):
    test_csv = tmp_path / "empty_file.csv"
    assert read_file_pandas(str(test_csv)) == ""


def test_read_file_pandas_error_not_exist():
    assert read_file_pandas("we_dont_have_this_file.csv") is None


