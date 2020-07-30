#Ask the user to input a,b,c for an equation ax**2 + bx + c
import math


a = int(input("Enter the coefficient of a: "))
b = int(input("Enter the coefficient of b: "))
c = int(input("Enter the coefficient of c: "))

#Displaying the values of a,b and c
print("a= "+a+", b= "+b+", c= "+c)

#Discriminant 
print("\nFirst we have to calculate the discriminant(d).")
print("d=b\u00b2 - 4ac = "+b+"\u00b2 - 4"+a+""+c)
discriminant = b**2-4*a*c 
print("==> d="+discriminant)

#Calculating the roots
if discriminant < 0:
	print("Since the discriminant<0, this equation has no real roots.")

elif discriminant == 0:
	print("Since the discriminant=0, this equation has only one root.")
	print("==> x= -b/2a")
	print("==> x= -"+b+"/2"+a)
    x = -b/2*a
    print("==> x="+x)
    print ("The root of this equation is ", x)

else:
	print("The equation has more than one root.")
	print("Root 1(x1)= -b+ sqrt(d) / 2a")
	print("==> -"+b+" + sqrt("+d+") /2"+a)
    x1 = (-b+math.sqrt(discriminant)/(2*a))
    print("==> x1=",x1)

    print("Root 2(x2)= -b - sqrt(d) / 2a")
	print("==> -"+b+" - sqrt("+d+") /2"+a)
    x2 = (-b-math.sqrt(discriminant)/(2*a))
    print("==> x2=",x2)

    print ("\nThe quadratic equation has two roots: ", x1, " or", x2)