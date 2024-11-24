from math import pi

valores = [1, 3, 0, -1, -3, 2+3j, True, 'Hola']

def area(r):
  areaC = pi*(r**2)
  return areaC

for v in valores:
  areaCalculada = area(v)
  print('Para el valor de', v, 'el area es', areaCalculada)
  

