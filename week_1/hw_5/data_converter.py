import argparse
import json
import sys
import os


ALLOWED_OPERATORS = ["<=", ">=", "==", "!=", "<", ">"]


def filter_data(data, field, expr, value):
    filtered_data = []
    if expr not in ALLOWED_OPERATORS:
        raise ValueError(f"Недопустимое выражение для фильтра, используйте {', '.join(ALLOWED_OPERATORS)}")

    try:
        value = float(value)
    except ValueError:
        raise ValueError(f"Значение {value} не число")

    for i in data:
        if expr == "<=":
            if float(i[field]) <= float(value):
                filtered_data.append(i)
        elif expr == ">=":
            if float(i[field]) >= float(value):
                filtered_data.append(i)
        elif expr == "==":
            if float(i[field]) == float(value):
                filtered_data.append(i)
        elif expr == "!=":
            if float(i[field]) != float(value):
                filtered_data.append(i)
        elif expr == "<":
            if float(i[field]) < float(value):
                filtered_data.append(i)
        elif expr == ">":
            if float(i[field]) > float(value):
                filtered_data.append(i)

    return filtered_data


def sort_data(data, field, order):
    sorted_data = []
    match field, order:
        case ["name", "asc"]:
            sorted_data = sorted(data, key=lambda x: x["name"])
        case ["name", "desc"]:
            sorted_data = sorted(data, key=lambda x: x["name"], reverse=True)
        case ["age", "asc"]:
            sorted_data = sorted(data, key=lambda x: int(x["age"]))
        case ["age", "desc"]:
            sorted_data = sorted(data, key=lambda x: int(x["age"]), reverse=True)
        case ["rate", "asc"]:
            sorted_data = sorted(data, key=lambda x: float(x["rate"]))
        case ["rate", "desc"]:
            sorted_data = sorted(data, key=lambda x: float(x["rate"]), reverse=True)
    return sorted_data


def find_data(data, names):
    found_data = []
    for i in data:
        if i["name"] in names:
            found_data.append(i)
    return found_data


def get_statistic(data):
    stats = {
        "avg_age": sum(int(i["age"]) for i in data) / len(data),
        "avg_rate": sum(float(i["rate"]) for i in data) / len(data),
        "students_cnt": len(data)
    }
    return stats


def main():
    parser = argparse.ArgumentParser(
        description="""
    Программа для фильтрации, сортировки, поиска и экспорта данных о студентах из CSV-файла.
    Файл должен содержать заголовки: name,age,rate

    Примеры:
      python script.py -f students.csv -a age >= 21 -s rate desc -o json
      python script.py -f students.csv -d Alice Bob -o html
      python script.py -f students.csv -s name asc -o json
    """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-f", "--filename", type=str, required=True, help="имя файла")
    parser.add_argument("-a", "--filter", type=str, required=False, nargs="*",
        help="""фильтрация, поле фильтрации указывается первым параметром [age/rate], выражение - вторым, значение - третьим. Пример age >= 20 (внимание: параметр фильтр может быть только один)"""
    )
    parser.add_argument("-s", "--sort", type=str, required=False, nargs="*",
        help="""сортировка, поле сортировки указывается первым параметром, тип сортировки вторым [asc/desc], (внимание: параметр сортировки может быть только один)"""
    )
    parser.add_argument( "-d", "--find", type=str, required=False, nargs="*",
         help="поиск по имени, возможно указание несколько имен через пробел"
    )
    parser.add_argument("-o", "--output", type=str, required=True,
        help="тип экспорта [json/html]")
    args = parser.parse_args()

    wrk_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    data = []
    data_dct = {}
    with open(f"{wrk_dir}/{args.filename}", "r", encoding="UTF-8") as file:
        content = file.read()
        content = content.splitlines()
        for row in content[1:]:
            row = row.split(",")
            data_dct["name"] = row[0]
            data_dct["age"] = row[1]
            data_dct["rate"] = row[2]
            data.append(data_dct.copy())

    # фильтрация
    if args.filter:
        data = filter_data(data, field=args.filter[0], expr=args.filter[1], value=args.filter[2])

    # сортировка
    if args.sort:
        data = sort_data(data, *args.sort)

    if args.find:
        data = find_data(data, args.find)

    # получение статистики
    stats = get_statistic(data)
    print(f"""
        Общая статистика:
        средний возраст: {stats.get("avg_age", None)} 
        средняя оценка: {stats.get("avg_rate", None)}
        количество студентов: {stats.get("students_cnt", None)}
    """)

    if args.output == "html":
        output_data = "<table border='1'>"
        for row in data:
            output_data += f"<tr><td>{row.get("name", None)}</td><td>{row.get("age", None)}</td><td>{row.get("rate", None)}</td></tr>"
        output_data += "</table>"
    elif args.output == "json":
        output_data = json.dumps(data, indent=2, ensure_ascii=False)
    else:
        raise ValueError("Ошибка. Недопустимый тип экспорта, должен быть html или json")

    with open(f"students.{args.output}", "w", encoding="UTF-8") as file:
        file.write(output_data)


if __name__ == "__main__":
    main()
