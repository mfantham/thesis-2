import math

lamda = 488e-9
theta = 80
n1 = 1.52
n2 = 1.33

E0 = 100
pi = 3.14159
e = 2.718281

z = 178e-9 #nm?

thetaR = theta * pi / 180

d = lamda / ( 4 * pi * ( n1**2 * math.sin(thetaR) - n2**2 ) ** (0.5) )
E = E0 * e ** ( -z / d )

print(str(d*10**9) + 'nm')
print(str(E) + '%')
