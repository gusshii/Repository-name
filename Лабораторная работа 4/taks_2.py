# TODO импортировать необходимые модули
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # TODO Считать содержимое csv файла
    with open(INPUT_FILENAME, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    headers = lines[0].split(",")

    data = []

    for line in lines[1:]:
        values = line.split(",")
        item = dict(zip(headers, values))
        data.append(item)

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output:
        json.dump(data, output, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
