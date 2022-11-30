number = []

while True:
    print("Enter numbers. (To finish press 'Enter' key)")
    n = input()
    if len(n) == 0 :
        break
    number.append(float(n))

number.sort()

median=0
idx=0

if len(number)%2==0:

    idx = int(len(number)//2)

    median=(number[idx-1]+number[idx])/2

else:

    idx = int(len(number)/2)

    median=number[idx]
    
print("You entered")
print(number)
print(" ")
print("max :", max(number))
print("min :", min(number))
print("median :", "%.2f"%median)

