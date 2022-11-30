class Account( ) :    
    def __init__(self, name, balance) : 
        self.name = name
        self.balance = balance

    def print_balance(self) : 
        print(" ")
        print("계좌소유자 : %s\n현재 잔액 : %s"% (self.name, self.balance))

    def deposit(self, amount) : 
        print(" ")
        amount = input("입금할 금액을 입력해주세요 : ")
        if int(amount) > 0:
            self.balance = self.balance + int(amount)
            print("{}원이 성공적으로 입금되었습니다.".format(amount))
        else:
            print("정확한 금액을 입력해주세요.")
        return self.balance

    def withdraw(self, amount) : 
        print(" ")
        amount = input("출금할 금액을 입력해주세요 : ")
        if int(amount) > 0:
            if int(amount) <= self.balance:
                self.balance -= int(amount)
                print("{}원이 성공적으로 인출되었습니다.".format(amount))
            else:
                print(" ")
                print("잔액부족, 거래가 거절되었습니다.")
        else:
            print("정확한 금액을 입력해주세요.")
        return self.balance
    
name = input("계좌 소유주의 이름을 입력해주세요 : ")
a = Account(str(name), 0)
amount = 0
            
menu = 0

while menu != 4:
    
    print(" ")
    print("================================")
    print("           Sookmyung Bank ATM")
    print("================================")    
    print("             1. 잔액확인")
    print("             2. 입금")
    print("             3. 출금")
    print("             4. 종료")
    print(" ")
    print("================================")
    print(" ")

    menu = int(input("메뉴를 선택해주세요 >>> "))
    
    while True:
        if menu ==1:
            a.print_balance()
            break
        elif menu == 2:
            a.deposit(amount)
            break
        elif menu == 3:
            a.withdraw(amount)
            break
        elif menu == 4:
            print("이용해주셔서 감사합니다.")
            break
        else:
            print("메뉴를 다시 선택해주세요.")
            print(" ")
            break
        
            
        
        
