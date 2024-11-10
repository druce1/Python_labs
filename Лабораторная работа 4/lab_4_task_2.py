import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        dict_reader = csv.DictReader(f)
        list_dict = [row for row in dict_reader]

    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(list_dict, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
