studno = input("Enter student number: ")
print("\n")
k = 0

for i in studno:
    num = int(i)
    if 1 < num < 9:
        for x in range(2, num):
            if (num % 2) == 0:
                break
        else:  
            k += 1 


print("1. There are ",k," prime numbers in the student number: ",studno,"\n")

import random
q = random.randrange(25,40,1)
print ("2. The random number is: ", q,"\n")

r = q / k
rr =round(float(r))
print("3. Number of strings to be generated is: ", rr,"\n") 

import string

def randomString(sl):
    letters=string.ascii_lowercase
    return ''.join(random.choice(letters) for t in range(sl))

rrr=round(float(r/2))
stringlist=[]
print("4. List of strings: ",rrr)

for z in range(rrr):
    stringlist.append(randomString(5))
    stringlist.append(randomString(7))

print("8==================D")
print(*stringlist, sep = "\n")
print("8==================D")

vList=[]
vowels=["a","e","i","o","u"]
for u in stringlist:
    vCount = 0
    for let in str(u):
        for v in vowels:
            if let == v:
                vCount += 1
                break
    vList.append(vCount)

for i in range(len(vList) -1):
    for j in range(len(vList) - int(i) -1):
        if vList[j] > vList[j+1]:
            temp = vList[j]
            vList[j] = vList[j+1]
            vList[j+1] = temp
            temp2 = stringlist[j]
            stringlist[j] = stringlist[j+1]
            stringlist[j+1] = temp2

print("5. Sort list: ")
print("8==================D")
lCount = 1
for p in range(len(stringlist)):
    lCount += 1

print("8==================D")

def reverseList():
    lCount = 0
    print("5. Sort in descending order: ")
    print("8==================D")
    stringlist.reverse()
    vList.reverse()
    for p in range(len(stringlist)):
        print(lCount, " - ", stringlist[p], "(Vowels: ", vList[p], ")")
        lCount += 1
    
reverseList()



            







