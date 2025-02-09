'''
Simple use case of the match functions as well as the __match_args__ class variable
https://docs.python.org/3/reference/datamodel.html#object.__match_args__
'''

class Point:
    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


points = [Point("Ricardo", 0), Point(0, [1, 2, 3])]  # Example input list of points

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(x1, y1), Point(x2, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}, {x1}, {x2}")
    case _:
        print("Something else")
