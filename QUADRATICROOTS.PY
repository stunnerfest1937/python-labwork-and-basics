
import math

a = int(input("enter the coefficiant of quadratic term term "))
b = int(input("enter the coefficiant of linear term  "))
c = int(input("enter the constant term "))
s = b * b - (4 * a * c)
v = math.sqrt(s)
x1 = (-b + math.sqrt(s)) / (2 * a)
x2 = (-b - math.sqrt(s)) / (2 * a)
print("roots of the quadratic equation are (", x1, x2, ")")

