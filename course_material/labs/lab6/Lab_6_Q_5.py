class Triangle():

    def __init__(self):
        self.base = 0
        self.height = 0
    def set_base(self, base):
        self.base = base
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return 0.5 * self.base * self.height
    def print_info(self):
        print("Base: ", self.base)
        print("Height: ", self.height)
        print("Area: ", self.get_area())
    def __lt__(self, other):
        return self.get_area() < other.get_area()

if __name__ == "__main__":
    triange1 = Triangle()
    triangle2 = Triangle()

    #get base and heightfrom command line
    triange1.set_base(3)
    triange1.set_height(4)
    triangle2.set_base(4)
    triangle2.set_height(5)
    print("Triangle with larger area:")
    if triange1 < triangle2:
        triange1.print_info()
    else:
        triangle2.print_info()