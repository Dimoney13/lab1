import sys
import math


def get_coef(i, name):
    s = sys.argv[i] if len(sys.argv) > i else input(f"Введите {name}: ")
    while True:
        try:
            return float(s)
        except ValueError:
            s = input(f"Некорректно. Введите {name} ещё раз: ")


a = get_coef(1, "A")
b = get_coef(2, "B")
c = get_coef(3, "C")

if a == 0:
    print("A = 0, уравнение не биквадратное")
    sys.exit()

d = b * b - 4 * a * c
print("Дискриминант D =", d)

roots = set()
if d >= 0:
    for t in [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]:
        if t >= 0:
            roots.add(math.sqrt(t))
            roots.add(-math.sqrt(t))

if roots:
    print("Корни:", *sorted(roots))
else:
    print("Действительных корней нет")