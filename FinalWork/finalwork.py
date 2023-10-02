## Задание. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.


import logging
import argparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class NegativeLengthError(Exception):
    pass


def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise NegativeLengthError("Стороны треугольника должны быть положительными.")
    return a + b > c and a + c > b and b + c > a


def triangle_type(a, b, c):
    if is_triangle(a, b, c):
        if a == b == c:
            return 'равносторонний'
        elif a == b or b == c or a == c:
            return 'равнобедренный'
        else:
            return 'разносторонний'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Определение типа треугольника по сторонам')
    parser.add_argument('--a', type=float, help='Длина стороны a', required=True)
    parser.add_argument('--b', type=float, help='Длина стороны b', required=True)
    parser.add_argument('--c', type=float, help='Длина стороны c', required=True)

    args = parser.parse_args()

    try:
        a, b, c = args.a, args.b, args.c
        logging.info(f'Проверка на существование треугольника со сторонами: {a}, {b}, {c}')

        if is_triangle(a, b, c):
            logging.info(f'Треугольник существует')
            print(f"Треугольник с сторонами {a}, {b}, {c} существует и он {triangle_type(a, b, c)}.")
        else:
            logging.warning(f'Треугольник не существует')
            print("Треугольник не существует.")

    except NegativeLengthError as e:
        logging.error(f'Ошибка: {e}')
        print(e)
