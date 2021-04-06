class Point:
    x=0
    y=0
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def print_point(self):
        print(self.x, self.y)

p = Point(3,4)

p.print_point()


class flight:
    passengers = []
    def __init__(self,capacity):
        self.capacity = capacity

    def addPassenger(self,name):
        if self.capacity>0:
            self.passengers.append(name)
            self.capacity -= 1
            print(f"added {name}")
        else:
            print("not added.. over capacity")

f = flight(10)
f.addPassenger("semih")
f.addPassenger("semih")
f.addPassenger("semih")
f.addPassenger("semih")
f.addPassenger("semih")
f.addPassenger("semih")
f.addPassenger("semih")
f.addPassenger("semih")
f.addPassenger("semih")
f.addPassenger("semih")
f.addPassenger("semih")