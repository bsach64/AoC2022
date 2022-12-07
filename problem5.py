crates = []
indicator = 0
x = 0
for i in range(0, 3):
    crates.append(['#'])
for i in range(0, 3):
    crates[i].append('#')
    crates[i].append('#')

'''with open("sampleday5", "r") as file:
    #for line in file:
        #for c in range(1, len(line), 4):
            #if line[c] != " ":'''
                


print(crates)
with open("sampleday5", "r") as file:
    for line in file:
        line.strip()
        indicator = indicator + 1
        if indicator <= 3:
            for i in range(1, len(line), 4):
                if line[i] == " ":
                    crates[x].append('#')
                else:
                    crates[x].append(line[i])
                x = x + 1

#print(crates)

#with open("sampleday5", "r") as file:
    #for line in file:
        #indicator = indicator + 1
        #line.strip()
        #if indicator <= 3:
            #crates.append([])
        #for i in range(1, len(line), 4):
            #if indicator <= 3:
                #if line[i] == " ":
                    #crates[-1].append('#')
                #else:
                    #crates[-1].append(line[i])

#print(crates)


                        

