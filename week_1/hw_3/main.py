import tasks_manager as tm


def parse_command(caption):
    allowed_ops = ["add", "remove", "show", "exit"]
    while True:
        user_input = input(caption)
        cmd = user_input.split()[0]
        if cmd.lower() == "exit":
            print("Выход")
            exit(0)
        if cmd in allowed_ops:
            content = user_input.replace(cmd, "", 1).strip()
            return cmd, content
        print("Ошибка: недопустимая команда, разрешено только add, remove, show, exit")


def main():
    tasks = []
    while True:
        command, content = parse_command("Введите команду (add, remove, show, exit): ")
        match command:
            case "add":
                tm.add_task(tasks, content)
            case "remove":
                tm.remove_task(tasks, content)
            case "show":
                tm.show_tasks(tasks)


if __name__ == "__main__":
    main()
