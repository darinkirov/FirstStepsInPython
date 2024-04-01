from math import pi
type = input()

if type == "square":
    duljina = float(input())
    lice = duljina * duljina
    print(f"{lice:.3f}")
elif type == "rectangle":
    x = float(input())
    y = float(input())
    area = x*y
    print(f"{area:.3f}")
elif type == "triangle":
    x = float(input())
    h = float(input())
    area = x*h/2
    print(f"{area:.3f}")
elif type == "circle":
    r = float(input())
    area = r*r*pi
    print(f"{area:.3f}")
else:
    print("error")