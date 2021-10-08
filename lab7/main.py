'''
1. Proszę napisać trzy funkcje generatorowe:
 - zwracającą kolejną liczbę naturalną (nieskończony),
 - zwracającą te wartości z przekazanej jako parametr sekwencji, które są 
   liczbami doskonalymi (liczby naturalne, która są sumą wszystkich swoich 
   dzielników wfaściwych)
 - zwracającą wartości z przekazanej jako pierwszy parametr sekwencji i 
   przerywającą dzialanie po napotkaniu wartości większej niż drugi 
   parametr przekazany do funkcji

 Korzystając ze zdefiniowanych funkcji proszę wypisać doskonałe liczby 
 naturalne mniejsze od 10000 (2p)

2. Proszę napisać generator obliczający u: wg zależności:
 u_i = u_(i-1) + a/x_(i-1) z wartością początkową u_0=0, dla x_0=1 oraz z x_i=x_0+i_a 
 Obliczenia proszę wykonać dla a=0.05 i przerwaćje dla x=1.5. Zależność 
 pozwala na wyznaczenie przybliżonej wartości logarytmu naturalnego z 
 danej liczby. Generator ma zwracać x oraz przybliżoną i dokładną wartość 
 logarytmu naturalego (2p)
*x_i - indeks dolny i


3. Każdą liczbę cafkowną można zapisaćjako sumę wartości cafkownych 
 mniejszych od niej samej, np. 4 można zapisaćjako: 1+1+1+1,1+1+2,1+3 
 oraz 2+2. Proszę napisać generator zwracający wszystkie możliwe sumy dla 
 określonej wartości n (2p)


4. Proszę napisać generator zwracający liczby spelniające warunek, że wartość 
 kolejna je, co najmniej o 0.4 mniejsza lub większa od wartości poprzedniej.
 Dzielenie generatora należy zakończyć, jeżeli wylosowana wartość je, 
 mniejsza od 0.1 (2p)

5. Proszę napisać generator dziafający dokfadnie tak samojak wbudowany 
 renge (proszę się upewnić,. wiecie Państwo jak on dzial,), ale 
 pozwalający na generowanie liczb rzeczywistych (2p)
 Do test.: range(8), range(,), range(1,8), range(8,1), range(1,8,2), 
 range(1,8,-2), range(8,1,2), range(3,1, 2)
 '''
print("zad1")
n = 1000
def gen1():
  i = 0
  while True:
    yield i
    i += 1

def if_perfect(a):
  sum = 1
  for i in range(2,a):
    if a%i == 0 :
      sum += i
  return True if sum == a else False

def gen2( sek ):
  for i in sek:
    if ( if_perfect(i) ):
      yield i

def gen3( sek, stop):
  for i in sek:
    if i > stop:
      break
    yield i

print( list(gen3(gen2(gen1()),n))) 


import math
print("\nzad2")
def gen4():
  u, x0 , a = 0.0, 1.0, 0.05
  i = 1
  x = 1.0
  while x <= 1.5:
    yield u , math.log(x)
    u = u + a/x
    x = x0 + i*a
    i = i + 1

for i in gen4():
  print(i)


print("\nzad3")
def gen5( num ):
  for i in range(num-1,0,-1):
    temp=num
    out=[]
    while i>0 :
      while temp>=i:
        out.append(i)
        temp-=i
      i=temp
    yield out


for i in gen5(4):
  print(i)
        

import random as rand
print("\nzad4")
def gen6():
  random_last = -10
  random_now = rand.random()
  while random_now > 0.1:
    if math.fabs(random_last - random_now) > 0.4 :
      yield random_now
      random_last = random_now
    random_now = rand.random()

print( list(gen6() ) )
  

print("\nzad5")
def gen_range(start, stop = None, step = None):
  start = float(start)
  if stop is None and step is None:
    stop = start
    step = 1.0
    start = 0.0
  
  if step is None:
    step = 1.0
  
  if start < stop:
    if step <= 0.0:
      return
    else:
      current = start
      while current < stop:
        yield current
        current += step
  
  else:
    if step >= 0.0:
      return
    else:
      current = start
      while current > stop:
        yield current
        current += step

 

print( "range(8)" )
print( list( range(8) ) )
print( list( gen_range(8) ) )

print( "range(-8)" )
print( list( range(-8) ) )
print( list( gen_range(-8) ) )

print( "range(1,8)" )
print( list( range(1,8) ) )
print( list( gen_range(1,8) ) )

print( "range(8,1)" )
print( list( range(8,1) ) )
print( list( gen_range(8,1) ) )

print( "range(1,8,2)" )
print( list( range(1,8,2) ) )
print( list( gen_range(1,8,2) ) )

print( "range(1,8,-2)" )
print( list( range(1,8,-2) ) )
print( list( gen_range(1,8,-2) ) )

print( "range(8,1,2)" )
print( list( range(8,1,2) ) )
print( list( gen_range(8,1,2) ) )

print( "range(8,1,-2)" )
print( list( range(8,1,-2) ) )
print( list( gen_range(8,1,-2) ) )



