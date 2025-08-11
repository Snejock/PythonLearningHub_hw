def add_task(tasks, title):
    if not tasks:
        tasks.append(
            (0, title),
        )
    else:
        max_id = max(tasks, key=lambda x: x[0])[0]
        tasks.append(
            (max_id + 1, title),
        )


def remove_task(tasks, index):
    try:
        idx = int(index)
        if idx in [i[0] for i in tasks]:
            for item in tasks:
                if item[0] == idx:
                    tasks.remove(item)
                    break
        else:
            print("Ошибка: индекс не найден")
    except ValueError:
        print("Ошибка: индекс должен быть числом")


def show_tasks(tasks):
    print("Список задач:")
    for item in tasks:
        print(f"{item[0]}: {item[1]}")
