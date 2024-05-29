'''Фабрика функций для сложения и вычитания:'''


def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y

        return add  # возвращаем функцию, как объект!! Тут скобки не нужны
    elif operation == "subtract":
        def subtract(x, y):
            return x - y

        return subtract


my_func_add = create_operation("add")
print(my_func_add(1, 2))

# Пример лямбда функции с аналогом через def
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Выводит 6


def multiply_def(x, y):
    return x * y


print(multiply_def(2, 3))  # Выводит 6


# Пример создания вызываемого объекта
class Repeater:
    def __init__(self, value):
        self.value = value

    def __call__(self, n):
        return [self.value] * n


repeat_five = Repeater(5)
print(repeat_five(3))  # Выводит [5, 5, 5]


# Умножить числа на 10
def multiply_10(n):
    def multiplier(x):
        return x * 10

    return multiplier


my_numbers = [3, 1, 4]
by_10 = multiply_10(10)
result = map(by_10, my_numbers)
print(list(result))

# Сложить 2 списка чисел
my_numbers = [3, 1, 4]
they_numbers = [2.4, 15, 0]

result = map(lambda x, y: x + y, my_numbers, they_numbers)
print(list(result))

# Из числа в списке вычесть 20

class Subtract:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n - x

my_numbers = [3, 1, 4]
sub = Subtract(20)
print(list(map(sub, my_numbers)))
