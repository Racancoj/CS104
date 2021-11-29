names = []
namesX = 0
while namesX != 10:
    names = input("pealse enter name ")
    namesX += 1
queue = []

for x in names:
    queue.append(x)
for x in range (len(names)):
    (queue.pop(0))


print (queue)
