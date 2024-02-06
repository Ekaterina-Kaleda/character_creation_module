from math import sqrt

message = ('Добро пожаловать в самую лучшую программу '
           'для вычисления квадратного корня из заданного числа')

print(message)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """
    Вычисляет квадратный корень введенного числа.

    Исключает отрицательные числа.
    """
    if your_number <= 0:
        root = 0
    else:
        root = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень',
          'из введённого вами числа.',
          f'Это будет: {root}')


calc(25.5)
