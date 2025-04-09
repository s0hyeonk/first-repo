sel = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 :"))
if sel == 1 :
    num = input("*** 수식을 입력하세요 :")
    result = eval(num)
    print(f"{num} 결과는 {result}입니다.")

elif sel == 2 :
    num1 = int(input("*** 첫 번째 숫자를 입력하세요 :"))
    num2 = int(input("*** 두 번째 숫자를 입력하세요 :"))
    result =sum(range(num1, num2 + 1))
    print(f"{num1}+...+{num2}는 {result}입니다.")

else :
    print("1 또는 2를 입력하세요")
    
