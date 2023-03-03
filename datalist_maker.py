import time

start = time.time()

datalist = ""

for a in range(8):
    for b in range(8):
        for c in range(8):
            for d in range(8):
                for e in range(8):
                    datalist += str(a+1) + " " + str(b+1) + " " + str(c+1) + " " + str(d+1) + " " + str(e+1) + " " + "10 "

print(datalist)

f = open("datalist.txt", "w")
f.write(datalist)

end = time.time()

print (str(end-start))
