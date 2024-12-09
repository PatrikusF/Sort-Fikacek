#Bubble sort
pole1 = [39, 12, 18, 85, 72, 10, 2, 16, 9, 24]

def bubble_sort():
   n = len(pole1)
   for a in range(n-1):
       for b in range(0, n-a-1):
           if pole1[b] > pole1 [b+1]:
               pole1[b], pole1[b+1] = pole1[b+1], pole1[b]
   print(pole1)
   return pole1
   
print("(Bubble) Seřazené pole1:", bubble_sort())
#-------------------------------------------------
#Bogo sort
import random

pole2 = [39, 12, 18, 85, 72, 10, 2, 16, 9, 24]
def is_sorted(pole2):
    for e in range (1, len(pole2)):
        if pole2[e] < pole2[e-1]:
             return False
    return True
def bogosort(pole2):
    count = 0      #"count" - zkontroluje zda výstupy programu odpovídají předloze
    while not is_sorted(pole2):
        random.shuffle(pole2)
        count += 1            #"+=" - přičítání hodnoty, celý zápis: x=x+1
        print(f"Pokus {count}: {pole2}")
    print(f"(Bogo) Seznam seřazen po {count} pokusech.")

bogosort(pole2)
print("(Bogo) Seřazené pole2:", pole2) 
#-------------------------------------------------
#Select sort
pole3 = [39, 12, 18, 85, 72, 10, 2, 16, 9, 24]

def selection_sort(pole3):
    n = len(pole3)
    for i in range(n):
        min = i           #"min"-minimální hodnota
        for j in range(i + 1, n):
            if pole3[j] < pole3[min]:
                min = j
        pole3[i], pole3[min] = pole3[min], pole3[i]
    return pole3

selection_sort(pole3)
print("(Select) Seřazené pole3:", pole3)
#-------------------------------------------------
#Insertion sort
pole4 = [39, 12, 18, 85, 72, 10, 2, 16, 9, 24]

def insertion_sort(pole4):
    for c in range(1, len(pole4)): 
        key = pole4[c]             #"key"-přiřazena hodnota prvku na indexu  
        d = c - 1                   
        while d >= 0 / pole4[d] > key:   #">=" - větší nebo rovno
            pole4[d + 1] = pole4[d]      #místo "/" může být i "and"
            d -= 1               #"-=" - odčítání a přiřazování     
        pole4[d + 1] = key

insertion_sort(pole4)
print("(Insertion) Seřazené pole4:", pole4)
