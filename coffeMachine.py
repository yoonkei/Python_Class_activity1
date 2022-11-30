print("======Sookmyung Cafe======")
print("  1. 아메리카노 1800원")
print("  2. 카페라떼   2200원")
print("  3. 카페모카   2800원")
print("==========================")
print(" ")

menu = 0
drink_1 = 0
drink_2 = 0
drink_3 = 0

while menu != 4:
    menu = int(input("메뉴를 선택해주세요 >>> "))
    if menu == 1:
        drink_1 = int(input("몇 잔을 주문하시겠습니까? >>> "))
        more = str(input("주문을 계속하시겠습니까? (Y/N) >>> "))
        if more == "y":
            print(" ")
            continue
        elif more == "Y":
            print(" ")
            continue
        elif more == "n":
            break
        elif more == "N":
            break
    if menu == 2:
        drink_2 = int(input("몇 잔을 주문하시겠습니까? >>> "))
        more = input("주문을 계속하시겠습니까? (Y/N) >>> ")
        if more == "y":
            print(" ")
            continue
        elif more == "Y":
            print(" ")
            continue
        elif more == "n":
            break
        elif more == "N":
            break
    if menu == 3:
        drink_3 = int(input("몇 잔을 주문하시겠습니까? >>> "))
        more = str(input("주문을 계속하시겠습니까? (Y/N) >>> "))
        if more == "y":
            print(" ")
            continue
        elif more == "Y":
            print(" ")
            continue
        elif more == "n":
            break
        elif more == "N":
            break    
    else:
        print("메뉴를 다시 선택해주세요.")
        continue

print(" ")
print("=====주문내역=====")
if drink_1 > 0:
    print("   아메리카노", drink_1, "잔")
if drink_2 > 0:
    print("   카페라떼: ", drink_2, "잔")
if drink_3 > 0:
    print("   카페모카: ", drink_3, "잔")    
print(" ")


Total = drink_1 + drink_2 + drink_3
Price = drink_1 * 1800 + drink_2 * 2200 + drink_3 * 2800
print(" ")
print("==총 ", Total, "잔, ", Price, "원==")
print(" ")
print("이용해주셔서 감사합니다.")
