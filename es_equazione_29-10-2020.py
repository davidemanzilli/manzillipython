import math

a = int(input("a = ?"))
b = int(input("b = ?"))
c = int(input("c = ?"))

delta = (b**2-4*a*c)

if delta < 0:
    print("non ci sono soluzioni")
else:
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print ("x1 è uguale a ", x1)
    print ("x2 è uguale a ", x2)




