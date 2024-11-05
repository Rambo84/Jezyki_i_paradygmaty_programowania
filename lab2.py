from unicodedata import numeric
#z1
def Zliczanie(tekst):
    slowa = 0
    zdania = 0
    akapity = 0
    lastlastChar = ""
    lastChar = ""
    id = 0
    for c in tekst:
        if lastChar == "\n":
            akapity += 1
        if (c == " " or c == "," or c == ";" or c == ":") and (lastChar != "-" or lastChar != "i" or lastChar != "oraz" or lastChar != "lub"):
            slowa += 1
        if c == ".":
            zdania += 1

        lastChar = c
        if id % 2 != 1:
            lastlastChar = c
        id += 1
    return slowa, zdania, akapity

print(Zliczanie("""Publikacja naukowa – artykuł w czasopiśmie naukowym lub w formie książki, spełniający określone, ostre kryteria poprawności, opisujący oryginalne badania naukowe i wynikające z nich wnioski, lub zbierający w formie przeglądu wnioski z wcześniej opublikowanych prac. Publikacje naukowe są zazwyczaj naukowym źródłem pierwotnym.

Struktura publikacji
W czasopismach naukowych spotyka się generalnie trzy rodzaje publikacji:

źródłowe – opisują badania własne autora lub zespołu naukowego, który bezpośrednio autorowi podlega,
przeglądowe – zbierają i konfrontują ze sobą wnioski z wielu publikacji źródłowych w celu usystematyzowania pewnego obszaru badań,
polemiczne – odnoszą się do wcześniejszych publikacji, kwestionując część zawartych w nich wniosków lub wiarygodność opisu zawartych w nich badań własnych.
Publikacja źródłowa
Źródłowa publikacja naukowa składa się zazwyczaj z następujących, stałych działów:

Tytułu, nazwisk autorów i ich adresów służbowych,
Abstraktu, czyli bardzo krótkiego (liczącego zwykle ok. 300 słów) opisu celu badań przedstawionych w artykule, ich metodyki, wyników oraz wniosków[1],
Listy słów kluczowych – ułatwiają odnalezienie artykułu w naukowych bazach danych,
Wstępu – będącego zwykle zwięzłym omówieniem obecnego stanu wiedzy w zakresie dotyczącym tematu publikacji i wyjaśnienia powodów podjęcia omawianych badań,
Opisu przeprowadzonych badań – musi być tak napisany, aby inni badacze mogli te badania powtórzyć i ewentualnie zweryfikować,
Wyniki – omawia się tu uzyskane rezultaty i relacje między nimi,
Dyskusja wyników – zamieszcza się obszerny opis przyjętej metodologii badań, syntezę otrzymanych wyników i wniosków wynikających z tych wyników,
Podsumowanie – gdzie streszcza się w krótkiej formie najważniejsze wnioski
Lista cytowań – lista dokładnych odnośników do prac, które zostały zacytowane lub wspomniane w publikacji
Publikacja przeglądowa
Układ publikacji przeglądowej różni się od publikacji źródłowej brakiem opisu przeprowadzonych badań a zamiast dyskusji wyników są kolejne rozdziały opisujące zestawione z sobą wnioski z innych publikacji. W podsumowaniu publikacji przeglądowej autor zamieszcza zwykle własne przemyślenia wynikające z zebranego materiału. Pozostałe działy publikacji przeglądowej wyglądają tak samo jak publikacji oryginalnej."""))

#z2
"""import numpy as np
A = np.array([[5], [3]])
B = np.array([[1, 2], [3, 4]])
C = np.array([[0, 1], [1, 1]])
print("Napisz działanie")
dzialanie = "A"#input()
wynik = eval(dzialanie)
print (wynik)
dzialanie = "~A"#input()
wynik = eval(dzialanie)
print (wynik)
dzialanie = "A & C"#input()
wynik = eval(dzialanie)
print (wynik)
dzialanie = "B | A"#input()
wynik = eval(dzialanie)
print (wynik)"""

#z3
def Naj(dane):
    liczba = list(filter(lambda x: isinstance(x, (int, float, complex)) and not isinstance(x, bool),dane))
    tekst = list(filter(lambda x: isinstance(x, str),dane))
    krotka = list(filter(lambda x: type(x) is tuple,dane))
    l = 0
    t = 0
    k = 0
    if liczba != None:
        max = 0
        for i in liczba:
            if i > max:
                max = i
        l = max

    if tekst != None:
        max = 0
        for i in tekst:
            if len(i) > max:
                max = len(i)
        t = max

    if krotka != None:
        max = 0
        for i in krotka:
            if len(i) > max:
                max = len(i)
        k = max

    return l, t, k

dane = ["tekscik", 24, 8, (1,3,4),"krotki",7,"długi tekst",13,"jj",("yy",4,15,18,20),(3,2)]
print()
print(Naj(dane))