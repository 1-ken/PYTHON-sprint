class Circle:
    # Initialize the Circle object with radius, perimeter, area, and pi
    def __init__(self, radius, perimeter=None, area=None, pi=3.142):
        # Store the radius, area, perimeter, and pi as instance variables
        self.radius = radius
        self.pi = pi
        self.area = area
        self.perimeter = perimeter

    # Calculate the area of the circle
    def calArea(self):
        # Calculate the area using the formula: area = pi * radius * radius
        self.area = self.pi * self.radius * self.radius
        # Print the area
        print("the area is: ", self.area)

    # Calculate the perimeter of the circle
    def Calperimeter(self):
        # Calculate the perimeter using the formula: perimeter = 2 * pi * radius
        self.perimeter = self.pi * 2 * self.radius
        # Print the perimeter
        print("the perimeter is:", self.perimeter)

# Get the radius from the user
rad = int(input('Enter the radius'))
# Create a Circle object with the given radius
circle1 = Circle(rad)
# Print the radius
print("radius is: ", circle1.radius)
# Calculate and print the area of the circle
circle1.calArea()
# Calculate and print the perimeter of the circle
circle1.Calperimeter()