import math
import time

def genNodes():
    print("node generating...")
    with open("./nodes-1k.csv", 'w+', encoding='utf-8') as nodeFile:
        # 1B = 10^9
        for i in range(pow(10, 3)):
            if(i%pow(10,7) == 0): print("{}% nodes generated.".format(i/pow(10,7)))
            nodeFile.write(str(i+1) + "\n")

def genEdges():
    print("edges generating...")
    with open("./edges-1k.csv", "w+", encoding='utf-8') as edgeFile:
        for i in range(pow(10, 3) - 2):
            if (i % pow(10, 7) == 0): print("{}% edges generated.".format(i / pow(10, 7)))
            edgeFile.write("{},{}\n".format(i+1,i + 2))
            edgeFile.write("{},{}\n".format(i+1, i + 3))

localtime1 = time.asctime( time.localtime(time.time()) )
print(localtime1)
genNodes()
localtime2 = time.asctime( time.localtime(time.time()) )
print(localtime2)
genEdges()
localtime3 = time.asctime( time.localtime(time.time()) )
print(localtime3)
print("-------start to generate nodes----------")
print(localtime1)
print("-------start to generate edges----------")
print(localtime2)
print("-------end----------")
print(localtime3)
