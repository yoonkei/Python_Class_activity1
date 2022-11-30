order = {'아메리카노' : 0, '카페라떼' : 0, '카페모카' : 0}
cmenu = ['아메리카노', '카페라떼', '카페모카']

def printCoffeeMenu(order):
    print(" ")
    print("[Cafe Menu]")
    print("아메리카노 1800원")
    print("카페라떼 2200원")
    print("카페모카 2800원")
    
def selectMenu(order):
    print(" ")
    while True:
        cafemenu = input("메뉴를 입력해주세요 (엔터입력시종료) >>> ")
        if cafemenu in cmenu:
            cup = input("몇잔을 주문하시겠습니까? >>> ")
            order[cafemenu] = int(order[cafemenu]) + int(cup)
            continue
        elif len(cafemenu) == 0:
            break
        else:
            print("메뉴를 다시 입력해주세요.")

def checkOrder(order):
    print(" ")
    for cafemenu in order:
        if order[cafemenu] >= 1:
            print(cafemenu, '\t', order[cafemenu], "잔")

def calculatePrice(order):
    global total
    global money
    total = int(order['아메리카노'] * 1800 + order['카페라떼'] * 2200 +order['카페모카'] * 2800)
    print("합계 : ", total)
    while True:
        money = int(input("지불할 돈: "))
        if money >= total:
            print("지불완료")
            break   
        else:
            print(total, "원 이상의 돈을 입력하세요.")

def getChange():
    print(" ")
    if total == money:
        print("잔돈은 0원 입니다.")
        print("================================")
    else:
        change = money - total
        print("잔돈은 {}원 입니다.".format(total))
        print("================================")
        fifty_count = change // 5000  
        ten_count = (change % 5000) // 1000  
        five_count = (change % 1000) // 500  
        one_count = (change % 500) // 100  
        print("5000원 : {}".format(fifty_count))
        print("1000원 : {}".format(ten_count))
        print("500원 : {}".format(five_count))
        print("100원 : {}".format(one_count))

total = 0
money = 0
change = 0


menu = 0

while menu != 4:
    
    print(" ")
    print("======Sookmyung Cafe============")
    print(" ")    
    print("             1. 커피 메뉴 선택")
    print("             2. 주문 내역 확인")
    print("             3. 결제")
    print("             4. 잔돈 계산")
    print(" ")
    print("================================")
    menu = int(input("메뉴를 선택해주세요 >>> "))
    if menu ==1:
        printCoffeeMenu(order)
        selectMenu(order)
    elif menu == 2:
        checkOrder(order)
    elif menu == 3:
        calculatePrice(order)
    elif menu == 4:
        getChange()
        print(" ")
        print("이용해주셔서 감사합니다.")
        break
        

