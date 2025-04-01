učebny = [1, 2, 3, 4, 5, 6]
x = len(učebny)
print(f"{x} učeben")
for i in (učebny):
    print(i)
add = int(input("Zadejte číslo učebny, kterou chcete přidat: "))
učebny.append(add)
učebny.remove(1)
učebny.sort()
učebny.reverse()
print(učebny)
