import json


def task() -> float:
    filename = "input.json"
    with open(filename) as f:
        data_json = json.load(f)

    total_sum = sum(data["score"] * data["weight"] for data in data_json)
    return round(total_sum, 3)


print(task())
