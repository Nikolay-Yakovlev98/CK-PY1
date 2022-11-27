import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_file, delimiter=",", new_line="\n") -> list[dict]:
    with open(input_file) as file:
        header = file.readline().replace(new_line, "").split(delimiter)
        data = []
        for line in file:
            data.append(line.replace(new_line, "").split(delimiter))
        last_data = []
        for i in range(len(data)):
            last_data.append(dict(zip(header, data[i])))
        return last_data


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
