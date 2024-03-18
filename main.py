from app.io.input import input_console, read_file, read_file_pandas
from app.io.output import output_console, add_to_file


def main():
    file = "data/yellow_coldplay.txt"
    empty_file = "data/empty_file.txt"
    file_pandas = "data/new_table.csv"
    input_1 = input_console()
    output_console(input_1)
    input_2 = read_file(file)
    output_console(input_2)
    input_3 = read_file_pandas(file_pandas)
    output_console(input_3)
    add_to_file(empty_file, input_1)
    input_empty_file = read_file(empty_file)
    output_console(input_empty_file)


if __name__ == "__main__":
    main()
