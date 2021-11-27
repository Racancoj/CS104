names = ["sam","therese","joe","marianna","marietta","tony","tina","Renne","jake","tim"]
queue = []
for x in names:
    queue.append(x)
print(queue)
for x in range (len(names)):
    print(queue.pop(0))


print (queue)
