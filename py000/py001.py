print("Hello, World!")

numeros = [1, 2, 3]
print(numeros)

# https://realpython.com/python-append/
import math
def square_root(numbers):
  result = []
  for number in numbers:
    result.append(int(math.sqrt(number)))
  return result

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(numbers)
print(square_root(numbers))

x = 2.974
print(math.ceil(x)) #arredondamento
print(math.fabs(-1))

print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))

import numpy as np
from scipy import special
x = np.linspace(-15,5,201)
ai, aip, bi, bip = special.airy(x)

import matplotlib.pyplot as plt
plt.plot(x, ai, 'r', label='Ai(x)')
plt.plot(x, bi, 'b--', label='Bi(x)')
plt.ylim(-0.5, 1.0)
plt.grid()
plt.legend(loc='upper left')
plt.show()