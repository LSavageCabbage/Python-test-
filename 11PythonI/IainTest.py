studno = input("Enter student number: ")
k = 0
primeList=[]

for i in studno:
    num = int(i)
    for x in range(2,10):
        isPrime = True
        for y in range(2,int(x**0.5)):
            if (x % y) == 0:
                isPrime = False
                print(num , "is not a prime number")                
                break
        if isPrime:
            primeList.append(x)
            k += 1

print(*primeList)
print("There are ",k," prime numbers in the student number: ",studno)



