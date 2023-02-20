a=int(input("Enter the sides of squre:"))
s_area=lambda a:a*a
print("Area of squre is:",s_area(a))
l=int(input("Enter the length of the reactangle:"))
b=int(input("Enter the breadth of the rectangle:"))
r_area=lambda l,b:l*b
print("Area of reactangle is:",r_area(l,b))
b=int(input("Enter the base of triangle:"))
h=int(input("Enter the height of the triangle:"))
t_area=lambda b,h:5*b*h
print("Area of trianle is:",t_area(b,h))