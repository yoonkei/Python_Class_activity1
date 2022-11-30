number = int(input("숫자를 입력해주세요: "))

i = 1

while i <= number:
    if i % 2 == 0 and i % 3 == 0:
        i = i + 1
        continue
    else :
        print(i)
        i = i + 1
        
        
