#z1
from ftplib import print_line
from operator import contains


def ProblemPaczek(wagi, maxWaga):
    wagi = sorted(wagi, reverse = True)
    if len(wagi) == 0:
        raise ValueError(f"Nie ma paczek do rozwiezienia")
        return

    if wagi[0] > maxWaga:
        raise ValueError(f"Paczka o wadze {wagi[0]} przekracza maksymalną dozwoloną wartość")
        return

    kursy = []
    for waga in wagi:
        dodano = False
        for kurs in kursy:
            if sum(kurs) + waga <= maxWaga:
                kurs.append(waga)
                dodano = True
                break
        if not dodano:
            kursy.append([waga])

    return len(kursy), kursy

wagi = [10, 15, 7, 8, 5, 20, 10]
maxWaga = 25
print(ProblemPaczek(wagi, maxWaga))
liczbaKursów, kursy = ProblemPaczek(wagi, maxWaga)
for i, kurs in enumerate (kursy, 1):
    print(f"Kurs {i}: {kurs} - suma wag: {sum(kurs)} kg")

#z2
def BFS(graf, start, end):
    unvisited = [(start, [start])]
    visited = set()
    while len(unvisited) > 0:
        cur, path = unvisited.pop(0)
        if cur == end:
            return path
        for ne in graf[cur]:
            if ne not in visited and ne not in unvisited:
                unvisited.append((ne,path + [ne]))
                visited.add(cur)

    return []

graf = {
    "A":["B","D"],
    "B":["C","D"],
    "C":["B","F"],
    "D":["A","B","E","F"],
    "E":["D","F"],
    "F":["C","D","E"]
    }
print()
print(BFS(graf, "B", "E"))

print()
"""
#
list = [1,2,3,4,5,6,6,4,3,23,2]
newLista = []
newList = [x ** 2 for x in list if x % 2 == 0]
print(newList)
#map() filter() reduce()
newList1 = list(map(lambda x: x * 2, newLista))
print(newList1)
newList2 = list(filter(lambda x: x % 2 == 0, newLista))
print(newList2)
newList3 = reduce(lambda x, y: x + y, newLista)
print(newList3)
input = "2+2-56+125"
output = eval(input)
print(output)

inputDate = ""
#exec(inputDate)#nie bezpieczne?
"""

