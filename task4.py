import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', linesep='\n') -> list[dict]:
    with open(filename) as f:
        rows = f.read().strip("\n").split(linesep)
        listofdicts = []
        columnnames = rows[0].split(delimiter)
        for row in range(1, len(rows)):
            currentrownums = rows[row].split(delimiter)
            numrow = len(currentrownums)
            listofdicts.append({columnnames[idx]: currentrownums[idx] for idx in range(numrow)})

        return listofdicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
