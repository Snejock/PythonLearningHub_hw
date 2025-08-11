def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Ошибка: недопустимо деление на ноль")
        return None
    return a / b


def get_operands(caption):
    while True:
        value = input(caption)
        if value.lower() == "exit":
            print("Выход")
            exit(0)
        try:
            return int(value)
        except ValueError:
            print("Ошибка: аргумент должен быть числом")


def get_operation(caption):
    allowed_ops = ["+", "-", "*", "/"]
    while True:
        op = input(caption)
        if op.lower() == "exit":
            print("Выход")
            exit(0)
        if op in allowed_ops:
            return op
        print("Ошибка: недопустимая операция, разрешено только +, -, *, /")


def main():
    print("Добро пожаловать в калькулятор! Введите 'exit' для выхода")
    while True:
        a = get_operands("Введите первое число: ")
        operation = get_operation("Введите операцию: ")
        b = get_operands("Введите второе число: ")

        match operation:
            case "+":
                print(f"Результат: {add(a, b)}")
            case "-":
                print(f"Результат: {subtract(a, b)}")
            case "*":
                print(f"Результат: {multiply(a, b)}")
            case "/":
                print(f"Результат: {divide(a, b)}")
            case _:
                print("Ошибка: неизвестная операция")


if __name__ == "__main__":
    main()
