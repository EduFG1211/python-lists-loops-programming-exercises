par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
par = par.replace(" ","")
par = par.lower()
#print(par)
for i in par:
    counts[i] = 0

for j in par:
    if counts[j] >= 0:
        counts[j] = counts[j] + 1

print(counts)


