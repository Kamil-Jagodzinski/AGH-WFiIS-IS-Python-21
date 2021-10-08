'''
zad1
Proszę napisać funkcję, która pozwoli na wypisanie:
- n początkowych wierszy pliku, 
- n końcowych wierszy pliku, co n-tego wiersza pliku, 
- n-tego słowa ze wszystkich wierszy
- n-tego znaku ze wszystkich wierszy. 
Nazwę pliku oraz n przekazujemy jako parametr do funkcji. 
Każdy podpunkt==jedna linia kodu (1.5p)

zad2
Odczytujemy wartości ze wszystkich plików, których nazwy rozpoczynają się od data i kończą
na in w katalogu bieżącym. Na wyjściu proszę utworzyć jeden plik z trzema kolumnami:
   pierwsza kolumna - numer wiersza,
   druga kolumna - uśredniona wartość z danego wiersza ze wszystkich plików (numpy.average),
   trzecia kolumna - odchylenie standardowe wartości z danego wiersza ze wszystkich plików       (numpy.std)
PLIKI TESTOWE: data.zip
data0.in data1.in ... data.out
2            3               0 2.5   0.5
3            3.5            1 3.25 0.25
5            5               2 5      0

zad3
Proszę napisać funkcję, tworzącą plik z instrukcjami pozwalającymi na wygenerowanie wykresu 
plików j.w. + wynikowego (łącznie z odchyleniem standardowym)*patrz niżej, 
proszę skorzystać z potrójnego cudzysłowa (1p)

zad4
Pliki o nazwach rok.in (rank.zip) zawierają informację o pozycji na liście rankingowej pewnych osób,
w kolejnych latach. Proszę utworzyć zbiorczy plik, w którym w pierwszej kolumnie znajdzie się 
"nazwisko", kolejne kolumny będą odpowiadały pozycja danej osoby na liście rankingowej w 
kolejnych latach, od 2000 do 2020 (2.5p)

2000.txt
ABC 2
DEF 1
GHJ 3
2001.txt
ABC 3
DEF 1
GHJ 2
KLM 4
rank.out
Nazwisko 2000 2001
ABC         2       3
DEF         1       1
GHJ         3       2
KLM         -       4

zad5
Proszę sporządzić histogram słów rozpoczynających się na daną literę alfabetu ze 
wszystkich plików pasujących do określonego wzorca w katalogu bieżącym, opcje 
wyświetlenia: sortowanie alfabetyczne bądź po liczbie słów (2.5p)
PLIKI TESTOWE: zad5A.in, zad5B.in
'''

print("zad1")
def fun1(src, n):
  with open(src,"r") as file:
    lines = file.readlines()
  print("pierwsze n:")
  print( lines[0:n] )

  print("\nostatnie n:")
  print( lines[-n:] )

  print("\nco n:")
  print( lines[::n] )

  print("\nco n-te slowo:")
  print( [i.split(" ")[n-1] for i in lines] )
  
  print("\nco n-ty znak n:")  
  print( [i[n-1] for i in lines])

fun1("plik1.txt", 2)


print("zad2")
import numpy as np
import glob

all_num = []
for src in glob.glob("data*.in"):
  with open(src,"r") as file:
    line = file.readlines()
    all_num.append( [float(i) for i in line] )

with open("zad2_odp.txt", "w") as out:
  for j in range(len( all_num[0])):
    val = []
    for i in range( len( all_num ) ):
      val.append( all_num[i][j] )
    out.write(str(i)+"  "+str(np.average(val))+"  "+str(np.std(val))+"\n")
out.close()

        
print("zad3")
file3 = open("zad3.txt", "w")
file3.writelines('''Matplotlib jest biblioteką do tworzenia wykresów (https://matplotlib.org/). Wykorzystamy ją do wygenerowania prostego wykresu. Poniżej minimum konieczne, aby ten cel osiągnąć:
  import matplotlib.pyplot as plt
  #wyrysowanie krzywej y(x), 'o' oznacza styl punktu
plt.plot(x, y, 'o')
#wyrysowanie krzywej y(x) wraz z niepewnościami
plt.errorbar(x, y, marker='*', yerr=dy)
#opis osi
plt.xlabel('x')
#zapis do pliku, format określony przez rozszerzenie w nazwie
plt.savefig('res.pdf')
A to może się przydać do łatwego wczytywania plików (ale dzisiaj można z tego skorzystać tylko w skrypcie generującym wykresy)
import numpy
x,y=numpy.loadtxt(nazwa, unpack=True)''')
file3.close()


print("zad4")
names=[]
rank=[]
year=0
for file in glob.glob("zad4/*.txt"):
  with open(file) as f:
    line = f.readlines()
    for data in line:
      if data.split()[0] not in names:
        names.append(data.split()[0])

for name in names:
  rank.append((name,[' ']*21))

for file in glob.glob("zad4/*.txt"):
  with open(file) as f:
    line = f.readlines()
    for data in line:
      for person in rank:
        if data.split()[0] is person[0]:
          person[1][year] = int(data.split()[1])
  year+=1

with open("rank.txt", "w") as out:
  out.write('Name\t')
  for i in range(2000,2021):
    out.write(f"{i} ")
  for i in rank:
    out.write(f'{i[0]}\t')
    for j in range(21):
      out.write(f"{i[1][j]} ")
    out.write('\n')

print("zad5")

from matplotlib import pyplot as pl

words = []
for src in glob.glob("zad5*.in"):
  with open(src,"r") as file:
    lines = file.readlines()
    for i in lines:
      for w in i.split(" "):
        words.append(w)

words.sort()
# print(words)

app = [1]
prev = words[0]
for i in words[1:]:
  if i == prev:
    app[-1] += 1
  else:
    app.append(1)
  prev = i

words = list(set(words))
# print(app)

pl.plot(words, app)
pl.show()