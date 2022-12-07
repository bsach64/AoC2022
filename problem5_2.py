crates = []

for i in range(0, 3):
    crates.append([])

with open("sampleday5", "r") as file:
    line_count = 0
    for line in file:
        if line_count < 3:
            line_count = line_count + 1
            x = 0
            for i in range(1, len(line), 4):
                if line[i] == " ":
                    x = x + 1
                else:
                    crates[x].append(line[i])
                    x = x + 1


print(crates)