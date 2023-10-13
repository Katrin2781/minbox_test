from math import pi, sqrt


class Figurs:
    def __init__(self):
        self.error = None

    def no_positive(self, num):
        if type(num) in [int, float]:
            if num >= 0:
                return True
            else:
                self.error ="Число должно быть положительным"
                return False
        else:
            self.error="Неверный тип данных"
            return False


class Circle(Figurs):
    def __init__(self, radius):
        self._radius = radius
        self.positive = self.no_positive(radius)

    # площадь круга
    def area(self):
        if self.positive:
            return round(pi*self._radius**2, 2)
        else:
            return self.error


class Triangle(Figurs):
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c
        self.positive_a = self.no_positive(a)
        self.positive_b = self.no_positive(b)
        self.positive_c = self.no_positive(c)
        self.ok = False

        if self.positive_a and self.positive_b and self.positive_c:
            if self._a+self._b > self._c and\
               self._a+self._c > self._b and\
               self._b+self._c > self._a:
                self.ok = True
        else:
            print(self.error)

    #площадь треугольника
    def area(self):
        if self.ok:
            p = (self._a+self._b+self._c)/2
            s = sqrt((p*(p-self._a)*(p-self._b)*(p-self._c)))
            return round(s,2)
        else:
            return 'Треугольник не существует'

    #Проверка на то, является ли треугольник прямоугольным
    def right_triangle(self):
        if self.ok:
            l = [self._a, self._b, self._c]
            a, b, c = sorted(l)
            return a > 0 and a**2+b**2 == c**2
        else:
            return 'Треугольник не существует'
