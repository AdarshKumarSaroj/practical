import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Create two Point objects
point1 = Point(3, 4)
point2 = Point(7, 1)

# Print the points
print("Point 1:", point1)
print("Point 2:", point2)

# Calculate and print the distance between the two points
print("Distance between Point 1 and Point 2:", point1.distance(point2))
