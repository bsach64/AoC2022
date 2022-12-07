characters = {'a', 'b', 'B'}
simple = "Bhavik"
x = 0

common = characters.copy() 
for i in common:
    for z in simple:
        if (z == i):
            x = x + 1
        else:
            characters.remove(i)

print(characters)

