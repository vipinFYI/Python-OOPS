

"""
OOPS concept using kettle class

"""


class Kettle:

    def __init__(self,make,price):
        self.make = make
        self.price = price
        self.on = False

    def switchOn(self):
        self.on = True

kenwood= Kettle("kenwood",250)
preethi = Kettle("preethi",620)

print(kenwood.price)
print(kenwood.make)
print(kenwood.on)
print(preethi.make)
kenwood.switchOn()
print(kenwood.on)

#calling by class definition
print("calling by class")
print(preethi.on)
Kettle.switchOn(preethi)
print(preethi.on)




