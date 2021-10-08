'''
zad1
Proszę utworzyć string składający się z elementów listy argv z wyłączeniem nazwy
programu. Jeżeli program został uruchomiony bez podania parametrów proszę wypisać na
ekran komunikat informujący o właściwym sposobie uruchomienia programu (1p)

zad2
Na podstawie wcześniej utworzonego stringa proszę utworzyć cztery listy: zawierającą
małe litery, zawierającą duże litery, zawierającą cyfry oraz zawierającą wszystko co nie jest
literą (2p)

zad3
Na podstawie utworzonej listy zawierającej małe litery proszę utworzyć listę małych liter
bez powtórzeń. Następnie proszę utworzyć nową listę, w której każdy element jest
dwuelementową krotką (litera, krotność jej wystąpienia w liście oryginalnej) (2p)
Otrzymaną w powyższym punkcie listę proszę wyświetlić w kolejności od najwyższej
krotności (1p)

zad4
Proszę utworzyć listę dwuelementowych krotek, w których pierwszy element jest liczbą
pobraną z listy cyft, drugi natomiast wartością funkcji liniowej ax+b dla danej liczby;
wartości współczynników proszę ustalić w następujący sposób: a równa się liczbie
samogłosek w stringu z punktu pierwszego, a b - liczbie spółgłosek tamże (2p)

zad5
Proszę obliczyć wartości parametrów prostej korzystając z metody najmniejszych
kwadratów (2p)
'''

import sys 

print('zad1')
if len(sys.argv) > 1 :
  tekst= ''.join(sys.argv[1:])
else:
  print("Prosze uruchomic skrypt z parametrem")

print('\nzad2')
male =[i for i in tekst if i.islower() ]
duze = [i for i in tekst if i.isupper() ]
liczby = [float(i) for i in tekst if i.isdecimal() ]
reszta = [i for i in tekst if not i.isalnum() ]

print(duze)
print(male)
print(liczby)
print(reszta)

print('\nzad3')
male_uni=[]
for i in male:
  if i not in male_uni:
    male_uni.append(i)

male_krotka = [ (i, male.count(i) ) for i in male_uni ]
print(male_uni)
print(male_krotka)

print('\nzad4')
male_krotka.sort(key = lambda x: x[1], reverse = True)
print(male_krotka)

print('\nzad5')
samo = 'AaEeIiUuOoYy'
A = 0 
B = 0
for i in male + duze :
  if i in samo:
    A += 1
  else :
    B += 1 

punkty = [ ( i, A*i + B )  for i in liczby]
print(punkty)

sredniax, sredniay, a, D ,b = 0,0,0,0,0

for i in punkty :
  sredniax += i[0] 
  sredniay += i[1] 
  
sredniax /= len(punkty)
sredniay /= len(punkty)

for i in punkty :
  a += i[1]*(i[0] - sredniax)
  D += (i[0] - sredniax)*(i[0] - sredniax)

a /= D
b = sredniay - a*sredniax

print(sredniax)
print(sredniay)
print(a)
print(b)


