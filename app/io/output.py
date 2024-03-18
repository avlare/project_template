

def output_console(output):
    """
    Print data in console

    Args:
         output(any): the information that will output
    """
    print(output)


def add_to_file(path, info):
    """
    Adds information to the file

    Args:
        path (str): path to the file
        info (any): data that will be added to the file

    Except:
        FileNotFoundError: if cannot find the file by this path
    """
    try:
        with open(path, 'w') as file:
            file.write(info)
    except FileNotFoundError:
        print(f"Cannot find a file in {path}")
        return
