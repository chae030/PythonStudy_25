answer = int(input("정답 입력하기 : "))
num = 0
while num != answer :
    num = int(input("예상 숫자를 입력하세요 : "))
    if num > answer :
        print("DOWN")
    elif num < answer :
        print("UP")
    else :
        print("정답!")

num = ""
while num != 1 :
    num = int(input("구구단 몇 단을 출력할까요? (종료 1) : "))
    if num == 1 :
        print("종료합니다.")
    else :
        for i in range(1,10) :
            print(str(num)+' * '+str(i)+' = '+str(num*i))
    