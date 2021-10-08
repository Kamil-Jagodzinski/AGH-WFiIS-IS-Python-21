'''
1. Proszę napisać program testujący alternatywne sposoby budowania zestawu wartości: 
pęta for, lista składana, funkcja map i wyrażenie generatorowe (składnia taka jak listy 
składanej tylko w miejsce nawiasów kwadratowych należy wstawić okrągłe; o generatorach 
będziemy mówić na kolejnych zajęciach). Dla każdego ze sposobów proszę utworzyć osobną 
funkcję tak, aby uzupełnić poniższy kod:

import time
import sys

powt=1000

N=10000

(.)

print(sys: version)

test=(forStatement, listComprehension, mapFunction, generatorExpression)

for testFunction in test
printftestFunction._name_liust(20), =>, tester(testFunciion))

gdzie: tester - funkcja wywołująca powt razy daną funkcję, w której tworzonych 
jest N wartości.

Proszę wykonać testy (wszystko w ramach tych samych funkcj):
dodawanie elementu
dodawanie elementu podniesionego do kwadratu
sumowanie elementów z wykorzystaniem pętli for
sumowanie z wykorzystaniem funkcji sum
konwersja obiektu map i generatora do listy

Do pomiaru czasu proszę użyć funkcji time_ns z modułu time. 
Otrzymane wyniki proszę dołączyć do wysyłanego programu (2p)

2 Proszę wyznaczyć wartość liczby pi metodą Monte-Carlo korzystając z funkcji fiter (2p)
koło o promieniu 1 wpisujemy w kwadrat o boku 2 i umieszczamy ich środki w początku układu
współrzędnych. Stosunek pól tych figur jest równy stosunkowi liczby trafień w ich obszar, 
przy losowaniu dużej. liczby punktów wewnątrz kwadratu.

3. Proszę znaleść:
«_ największą wartość w każdym wierszu macierzy (map),
o. największą wartość w każdej kolumnie macierzy (map+zip),
«_ sumę dowolnej liczby macierzy macierzy (map+zip+lista składana)

Każde polecenie jedna linijka (2p)

4. Mamy listę, której elementami są listy dwuelementowe (możemy je potraktować jako 
współrzędne punktów na płaszczyźnie). Chcemy utworzyć nową listę, w której pierwszym 
elementem jest lista x-ów, a drugim lista y-ów. Proszę to zrobić w jednej linijce 
korzystając z funkcji reduce, wyrażenia lambda oraz wbudowanej funkcji map
(obie listy tworzymy jednocześnie!) (2p)

5. Proszę napisać funkcję przyjmującą dwa parametry lista x+ów i y-ów. Korzystając 
z funkcji wbudowanych reduce i map proszę obliczyć (i zwrócić z funkcji) wartości 
dofitowanych współczynników prostej oraz ich niepewności (wzory w pliku) (2p)
'''
import time
import sys
powt=1000
N=10000

print("zad1\n")
def forStatement():
  out = []
  for i in range(N):
    out.append(i)
  return out 

def listComprehension():
  out = [i for i in range(N)]
  return out 

def mapFunction():
  out = map(lambda i: i, range(N))
  return sum(out) 

def generatorExpression():
  out = (i for i in range(N))
  return sum(out) 

def tester(fun):
  start = time.time_ns()
  for i in range(powt):
    fun()
  return time.time_ns() - start

print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)

for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))



print("\nzad2\n")
import random as rand
import numpy as np
pts = [(rand.uniform(-1,1), rand.uniform(-1,1)) for i in range(5000) ]

def dist_from_0( xy ):
  return np.sqrt(xy[0]**2 + xy[1]**2)

in_circle = len( list ( filter(lambda x: dist_from_0(x)<= 1 ,  pts ) ) )
 
my_PI =  (in_circle) * 4.0/ len(pts)

print("Otrzymana wartosc PI:\n", my_PI)



print("\nzad3\n")

m1 = [ [1,2,1], [5,4,6], [1,2,1] ]
m2 =[ [2,1,3], [7,0,0], [1,9,9] ]
print( list( map( max, m1))) 
print( list( map( max, zip(*m1)) ) ) 
print( [list (map( max, zip(*i))) for i in zip(m1, m2)] )  



print("zad4\n")

import functools as ft

lista = [ [1,11], [2,12], [3,13] ]
#


print("zad5\n")
import math
list_x = [1,2,3,4,5]
list_y = [5,7,10,11,12]

def funkcja5(x, y):
  sr_x = ft.reduce(lambda a,b: a+b, x) / len(x)
  sr_y = ft.reduce(lambda a,b: a+b, y) / len(y)
  D = ft.reduce(lambda a,b: (sr_x - a)**2, x)
  A = ft.reduce(lambda a,b: a+b, list(map(lambda a,b: b*(a-sr_x), x, y)))/D 
  B = sr_y - A*sr_x
  y_err = math.sqrt(ft.reduce(lambda a,b: a+b, list(map(lambda a,b:(b-A*a-B)**2,x,y)))/len(x)-2)
  A_err = y_err/math.sqrt(D)
  B_err = y_err*math.sqrt( 1/len(x) + (sr_x**2)/D )
  print("A =", A)
  print("B =", B)
  print("Niepewność A =", A_err)
  print("Niepewność B =", B_err)

funkcja5(list_x, list_y)