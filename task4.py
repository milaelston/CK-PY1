import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter: str = ',', linesep: str = '\n') -> list[dict]:
    """Конвертер из cvs в json формат.

    :param filename: файл, из которого считываются данные
    :param delimiter: разделитель между значениями, по умолчанию ","
    :param linesep: разделитель строк, по умолчанию "\n"
    :return: список словарей json формата с данными из файла 
    """
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
