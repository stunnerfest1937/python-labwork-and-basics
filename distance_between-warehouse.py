import math
x1 = 2
y1 = 3
print("first warehouse is at point (2,3)")
x2 = 8
y2 = 11
print("second warehouse is at point (8,11)")
d = math.pow(x2 - x1, 2)
e = math.pow(y2 - y1, 2)
c = math.sqrt(d + e)
print("distance between two warehouses is ", c)
