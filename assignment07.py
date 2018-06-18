#Q1 Create a function to calculate the area of a circle by taking radius from user
def area():
    r = int(input("enter the radius: "))
    z = 2*3.14*(r**2)
    print(z)
area()
print("\n")


#Write a function “perfect()” that determines if parameter number is a perfect number.

p = []
def perfect():
	for x in range (1,1000):
		l = []
		s = 0	
		for y in range (1,x):
			if x % y == 0:
				l.append(y)
		for a in l:
			s=s+a
		if s == x:
			p.append(x)
perfect()
print(p)
print("\n")
		
		

#Q3 Print multiplication table of 12 using recursion		

def table(n):
	if n>10:
		return n
	else:
		print(12*n)
		table(n+1)
table(1)
print("\n")	

#4 Write a function to calculate power of a number raised to other ( a^b ) using recursion	

b = int(input("enter a base: "))
p = int(input("enter a power: "))
def power(x,y):
	return x**y
print(power(b,p))
print("\n")			
	
	

#Q5 Write a function to calculate power of a number raised to other ( a^b ) using recursion

a = int(input("enter a base: "))
b = int(input("enter a base: "))	
def fact (x):
	if x==1:
		return 1
	else:
		x = x*fact(x-1)
		return x
a = int(input("enter a number: "))
f = fact(a)	
print(f)
d = {}
print(d)	

	

