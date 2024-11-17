#Assignment
# Triangle Classifier
side1 = float (input("Enter the Length of the side 1:"))
side2 = float (input("Enter the Length of the side 2:"))
side3 = float (input("Enter the Length of the side 3:"))

if side1 == side2 == side3:
    print("equilateral triangle")
elif side1 == side2 or side1 ==side3 or side2 == side3:
    print("Iso scalas triangle")
else:
    print("scalene")