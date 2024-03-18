from pandas import read_csv


def input_console():
    """
    Reads information that the user enters from the console

    Returns:
        str. input from the user
    """
    inp = input()
    return inp


def read_file(path):
    """
    Reads information from the file

    Args:
        path (str): path to the file

    Except:
        FileNotFoundError: if cannot find the file by this path

    Returns:
        list of str. list of strings from the file
    """
    try:
        with open(path) as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"Cannot find a file in {path}")
        return


def read_file_pandas(path):
    """
    Reads information from the file using pandas

    Args:
        path (str): path to the file

    Except:
        FileNotFoundError: if cannot find the file by this path

    Returns:
        list of str. list of strings from the file
    """
    try:
        file_content = read_csv(path)
        return file_content
    except FileNotFoundError:
        print(f"Cannot find a file in {path}")
        return
