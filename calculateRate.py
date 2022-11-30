name = input("사용자 이름을 입력해주세요 :")
call = int(input("통화량(초)를 입력하세요 :"))
data = int(input("데이터 사용량(MB)를 입력하세요 :"))
charge = 12100
bill = charge +1.98 * call + 55 * data 
print(name,"님의 이번달 요금 :", bill)
