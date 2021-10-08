'''
1. Proszę napisać funkcję przyjmującą jako parametr string (przy wywołaniu 
będziemy przekazać argument wiersza poleceń). Zakładamy,że string ten zawiera 
poprawną definicję wyrażenia/funkcji matematycznej z jedną zmienną x,
czyli np. 'a•x+b','a*x**2+b*x+c'.w miejscu wszystkich stałych proszę wstawić 
losowe liczby całkowite z przedziału [O,1O),proszę wykorzystać metodę translate. 
Z funkcji proszę zwrócić listę dwuelementowych krotek (x,f(x)), 
dla 1O losowych liczb rzeczywistych z przedziału [O,1] (2p)."

2. Proszę napisać funkcję,do której można przekazać zmienną liczbę parametrów, 
zwracającą listę. Do wynikowej listy trafiają elementy, które powtarzają się 
we wszystkich parametrach przekazanych do funkcji, 
np.((1,2,3]. (1,3,5),(3,2]) -> [3]. 
((1,2,3],(1,3,5),(3,2,1]) -> (1,3]."
Proszę użyć konstrukcji for-else (2p)

3. Proszę napisać funkcję przyjmującą dwie sekwencje i parametr z 
wartością domyślną True. Funkcja zwraca listę dwuelementowych krotek 
zawierających elementy o tych samych indeksach z obu sekwencji. 
Jeżeli wartość trzeciego parametru wynosi True, długość zwracanej 
listy równa jest długości krótszej z przekazanych sekwencji, w przeciwnym 
wypadku brakujące elementy w krotkach uzupełniamy wartością None. 
Budowanie każdej z wynikowych list jedna linijka, proszę nie u
żywać funkcji wbudowanych!(2p)"

4. Proszę napisać funkcję umożliwiającą rozmienienie kwoty pieniędzy 
przekazanej jako jej pierwszy parametr nominałami określonymi poprzez 
drugi parametr - wartość domyślna krotka (10,5,2) 
(algorytm zachlanny).
Proszę sprawdzić działanie funkcji przekazując inny zestaw monet (2p)

5. Proszę napisać funkcję przyjmującą cztery parametry: liczba całkowita, 
której warość zgadujemy,granice przedzialu,w którym szukana liczba się 
mieści iostatni określający sposób poszukiwania wartości z wanością domyślną 'r'. 
Przy warości domyślnej ostatniego parametru,liczby poszukujemy losując kolejną warość, 
w innym przypadku poszukujemy wartości poprzez podział przedziału poszukiwania 
wartości na pół. W obu przypadkach w każdym kroku odpowiednio zawężamy przedział 
poszukiwania (proszę wykorzystać operator trójargumentowy).
Proszę sprawdzić ile kroków jest potrzebnych do"
znalezienia szukanej wartościw zależnościod metody (2p)
'''

import random
import string
import sys

print("zad1")
if len(sys.argv) > 1 :
  to_solve = sys.argv[1]
else:
  print("Prosze uruchomic skrypt z parametrem")

def funkcja1(arg):
  val = [random.random() for _ in range(10)]
  param=''.join(i for i in arg if i in string.ascii_lowercase)
  eq=str.maketrans(param, '0'*len(param))
  for i in eq:
    eq[i]=48 + random.randint(0,9)
  arg=arg.translate(eq)
  print(arg)
  return [(x,eval(arg)) for x in val]

print("Test1:", funkcja1(to_solve))


print("zad2")
def funkcja2(*arg):
  out = []
  for j in arg[0]:
    for k in arg:
      if j not in k:
        break
    else:
        out.append(j)
  return out

a ,b, c =  (1,2,3),(1,2,4,3),[1,3,6,7] 

print("Test2:", funkcja2(a,b,c) )


print("zad3")
def funkcja3(s1, s2, mode = True):
  if mode :
    return [ (s1[i],s2[i]) for i in range( min(len(s1), len(s2))) ]
  else:
    return [ (s1[i],s2[i]) if i <min(len(s1), len(s2)) else (None,s2[i]) if i>=len(s1) else (s1[i],None) for i in range(max(len(s1), len(s2))) ]

k1 = [1,2,3]
k2 = ['a','b']
print("Test3:", funkcja3(k1,k2) )
print("Test3:", funkcja3(k1,k2, mode = False) )


print("zad4")
def funkcja4(suma, nominaly = (10,5,2)):
  out = []
  i = 0 
  while suma >= 0:
    if suma >= nominaly[i]:
      suma -=nominaly[i]
      out.append(nominaly[i])
    elif i+1 < len(nominaly):
      i+=1
    elif suma > 0:
      return str(f'Nie można rozmienić: Wydano {out}, zostaje {suma} reszty')
    else:
      return out

print("Test4:", funkcja4(8) )
print("Test4:", funkcja4(14, (6,3,1)) )


print("zad5")
def funkcja5(to_find, left, right, mode = 'r'):
  steps = 0
  found = False
  while (not found) :
    steps += 1
    if mode == 'r':
      x = random.randint(left,right)
      if x == to_find:
        found = True
      left =  x+1 if x<to_find else left 
      right =  x-1 if x>to_find else right
    else:
      x = (left+right)//2
      if x == to_find:
        found = True
      left =  x if x<to_find else left 
      right =  x if x>to_find else right
  return f"Szukana liczba to {x} wykonane kroki: {steps}"


print("Test5:", funkcja5(2, 0, 8) )
print("Test5:", funkcja5(2, 0, 9, mode='b'))
