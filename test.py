import time

start = time.time()

f = open("datalist.txt")
ot = f.read().split(" ")

print(ot)

end = time.time()
print(len(ot))
print(str(end-start))
