import unittest
from square import Circle, Triangle
from math import pi, sqrt


class TestCircle(unittest.TestCase):
    def test_area(self):
        c = Circle(3)
        self.assertEqual(c.area(),round(pi*3**2,2))
        c = Circle(1)
        self.assertEqual(c.area(),round(pi,2))
        c = Circle(0)
        self.assertEqual(c.area(),0)
        c = Circle(2.5)
        self.assertEqual(c.area(),round(pi*2.5**2,2))
        c = Circle(-2)
        self.assertEqual(c.area(), 'Число должно быть положительным')
        c = Circle("2")
        self.assertEqual(c.area(), "Неверный тип данных")



class TestTriangleArea(unittest.TestCase):
    def test_area(self):
        t = Triangle(4, 2, 5)
        p = (4+2+5)/2
        s = round(sqrt((p*(p-4)*(p-2)*(p-5))),2)
        self.assertEqual(t.area(), s)
        self.assertEqual(t.right_triangle(), False)
        t = Triangle(4, 3, 5)
        self.assertEqual(t.right_triangle(), True)
        t = Triangle(4, -2, 5)
        self.assertEqual(t.area(), 'Треугольник не существует')
        t = Triangle("4", 2, 5)
        self.assertEqual(t.area(), 'Треугольник не существует')
