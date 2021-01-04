from abc import ABCMeta, abstractmethod
import wx
import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @property
    def xy(self):
        return self.x, self.y

    def __str__(self):
        return "x={0}, y={1}".format(self.x, self.y)

    def __repr__(self):
        return str(self.xy)

    @staticmethod
    def dist(a, b):
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


class Polygon(object):
    __metaclass__ = ABCMeta

    def __init__(self, points_list, **kwargs):
        for point in points_list:
            assert isinstance(point, Point), "input must be type Point"
            self.points = points_list[:]  # entire list
            self.points.append(points_list[0])
            self.color = kwargs.get('color', '#000000')

    def drawPoints(self):
        points_xy = []
        for point in self.points:
            points_xy.append(point.xy)
        print(points_xy)
        return tuple(points_xy)

    @abstractmethod
    def area(self):
        raise ("not implement")

    def __lt__(self, other):
        assert isinstance(other, Polygon)
        return self.area < other.area


class Rectangle(Polygon):
    def __init__(self, startPoint, w, h, **kwargs):
        self._w = w
        self._h = h
        Polygon.__init__(self,
                         [startPoint, startPoint + Point(w, 0), startPoint + Point(w, h), startPoint + Point(0, h)],
                         **kwargs)

    def area(self):
        return self._w * self._h


class TriAngle(Polygon):
    def __init__(self, top, left, right, **kwargs):
        self.top = top
        self.left = left
        self.right = right
        Polygon.__init__(self, [top, left, right], **kwargs)

    def area(self):
        a = Point.dist(self.top, self.right)
        b = Point.dist(self.top, self.left)
        c = Point.dist(self.left, self.right)
        s = (a + b + c) // 2

        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Example(wx.Frame):
    def __init__(self, title, shapes):
        super(Example, self).__init__(None, title=title, size=(600, 400))
        self.shapes = shapes
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Centre()
        self.Show()

    def OnPaint(self, e):
        dc = wx.PaintDC(self)

        for shape in self.shapes:
            dc.SetPen(wx.Pen(shape.color))

        dc.DrawLines(shape.drawPoints())


if __name__ == '__main__':
    prepare_draws = []
    start_p = Point(50, 60)
    a = Rectangle(start_p, 100, 80, color="#ff0000")
    prepare_draws.append(a)

    for shape in prepare_draws:
        print(shape.area())

    app = wx.App()
    Example('Shapes', prepare_draws)
    app.MainLoop()
