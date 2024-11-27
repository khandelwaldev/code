import math

def mathFunctions():
    print('Maths in python')
    
number = 16
print(f'square root of number {16} is {math.sqrt(number)}')

base = 2
exponent = 3
print(f'{base} raised to power {exponent} is {math.pow(base, exponent)}')
print(f'log base {base} of {math.pow(base, exponent)} is {math.log(math.pow(base, exponent), base)}')

angleDeg = 45
print(f'Sin of {angleDeg} deg is {math.sin(math.radians(angleDeg))}')
print(f'Cos of {angleDeg} deg is {math.cos(math.radians(angleDeg))}')
print(f'Tan of {angleDeg} deg is {math.tan(math.radians(angleDeg))}')

print(f'Value of pi: {math.pi}')
print(f"Value of e (Euler's number): {math.e}")