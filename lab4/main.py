'''
zad1
Proszę utworzyć k-elementową listę całkowitych wartości losowych z przedziału [0,5k).
Proszę sprawdzić ile elementów pozostaje na swoim miejscu po losowym przemieszaniu listy, 
mieszanie proszę wykonać 100 razy a wyniki zapisywać w słowniku (2p)

zad2
Proszę utworzyć losowy string o długości k zawierający tylko małe litery, 
pomiędzy poszczególne litery proszę wstawić kropkę (1p)

zad3
Proszę utworzyć listę stu wartości losowych z przedziału [0,20). 
Następnie na jej podstawie proszę utworzyć słownik, w którym klucze są liczbami z listy, a wartościami lista ich indeksów.
w rozwiązaniu proszę wykorzystać metodę setdefault i funkcjię enumerate (1.5p)
w rozwiązaniu proszę wykorzystać metody setdefault i index (1.5p)

zad4
Proszę sprawdzić ile spośród 1000 losowych wartości całkowitych składających się z n cyfr, 
gdzie n jest z przedziału [3,6], jest liczbami palindromowymi. Wynik proszę zapisać w słowniku (2p)

zad5
Proszę utworzyć dwa słowniki o rozmiarze 10, w których kluczami są kolejne liczby naturalne, 
a wartościami liczby losowe z przedziału [1,100). Następnie w obu słownikach proszę 
zamienić miejscami klucze z wartościami. Na podstawie tak otrzymanych słowników proszę 
utworzyć nowy słownik, w którym klucze są kluczami występującymi jednocześnie w obu 
wcześniej utworzonych słownikach, wartościami natomiast są dwuelementowe krotki wartości
związanych z danym kluczem w słownikach oryginalnych  (2p)
'''

import random
import copy
import string

print('zad1')
k = 6
list1 = [random.randint(0, 5*k - 1) for i in range(k)]

list_copy = copy.deepcopy(list1)

results = dict.fromkeys(range(100),0)

for i in range(100):
  random.shuffle(list_copy)
  for j in range(len(list_copy)):
    if list_copy[j] is list1[j]:
      results[list1[j]] += 1

print(results)


print('zad2')
str2 = ''
str2 += '.'.join(random.choice(string.ascii_lowercase) for i in range(k))
print(str2)


print('zad3')
list3 = [random.randint(0,19) for i in range(100)]
dict3a = {}
dict3b = {}

for i, j in enumerate(list3):
  dict3a.setdefault(j,[]).append(i)

for i in list3:
  dict3b.setdefault(i,[]).append(list3.index(i)) 

print(dict3a)
print(dict3b)


print('zad4')

def palindrom(x):
  xstr = str(x)
  for i in range(len(xstr)//2):
    if xstr[i] is not xstr[len(xstr)-1-i]:
      return False
  return True

rand_num = [random.randint(10**3,10**6+1) for _ in range(1000)]
dict4 = {"Palindrom": 0,
         "Nie Palindrom": 0}

for i in rand_num:
  if palindrom(i):
    dict4["Palindrom"] += 1
  else:
    dict4["Nie Palindrom"] += 1

print(rand_num)
print(dict4)


print('zad5')
dict5a = dict((i, random.randint(1,100)) for i in range(1,11))
dict5b = dict((i, random.randint(1,100)) for i in range(1,11))

dict5a = dict((dict5a[i], i) for i in range(1,11))
dict5b = dict((dict5b[i], i) for i in range(1,11))

dict5_result = dict((i,(dict5a[i], dict5b[i])) for i in dict5a if i in dict5b )

print(dict5a)
print(dict5b)
print(dict5_result)
