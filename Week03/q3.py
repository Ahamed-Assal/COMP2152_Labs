print("=" * 98)
print("Question 3: Cordinate System (Tuples)")
print("=" * 30)

point1 = (3, 5)
print("The Point 1 is: ", point1)

point2 = (7, 2)
print("The Point 2 is: ", point2)

x1, y1 = point1
print("x1= ", x1, ", y1= ", y1)

x2, y2 = point2
print("x2= ", x2, ", y2= ", y2)

distance = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
print("Distance between the points: ", distance)