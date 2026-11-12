import sys
import math


class BiquadraticEquation:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.roots = []

    def discriminant(self):
        return self.b * self.b - 4 * self.a * self.c

    def solve(self):
        d = self.discriminant()
        result = set()
        if d >= 0:
            t1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            t2 = (-self.b - math.sqrt(d)) / (2 * self.a)
            for t in [t1, t2]:
                if t >= 0:
                    result.add(math.sqrt(t))
                    result.add(-math.sqrt(t))
        self.roots = sorted(result)
        return self.roots

    def print_result(self):
        print("Дискриминант D =", self.discriminant())
        if self.roots:
            print("Корни:", *self.roots)
        else:
            print("Действительных корней нет")


class CoefReader:

    @staticmethod
    def get_coef(i, name):
        s = sys.argv[i] if len(sys.argv) > i else input(f"Введите {name}: ")
        while True:
            try:
                return float(s)
            except ValueError:
                s = input(f"Некорректно. Введите {name} ещё раз: ")

    def read_all(self):
        a = self.get_coef(1, "A")
        b = self.get_coef(2, "B")
        c = self.get_coef(3, "C")
        return a, b, c


def main():
    reader = CoefReader()
    a, b, c = reader.read_all()

    if a == 0:
        print("A = 0, уравнение не биквадратное")
        return

    equation = BiquadraticEquation(a, b, c)
    equation.solve()
    equation.print_result()


if __name__ == "__main__":
    main()