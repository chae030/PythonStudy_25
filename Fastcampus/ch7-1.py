# 튜플 조작기 ver 1

print("튜플 조작기 ver 1\n튜플에 입력할 자료들을 차례로 입력하세요. 빈칸으로 구분합니다.")
t = input()
t = tuple(t.split())
print(t)

while True :
    x = input("\n작업 할 내용을 입력하세요.\nq = 끝내기, s = 슬라이싱, c = 세기, i = 존재여부 : ")
    if x == "q" :
        print("프로그램을 종료합니다.")
        break
    elif x == "s" :
        fr = int(input("From : "))
        to = int(input("To : "))
        print(t[fr:to])
        continue
    elif x == "c" :
        co = input("찾을 자료 값은? : ")
        if co not in t : 
            print("찾으시는 자료가 존재하지 않습니다.")
        else :
            print(f"{t.count(co)}번 존재합니다.")
        continue
    elif x == "i" :
        index = input("찾을 자료 값은? : ")
        if index not in t :
            print("찾으시는 자료가 존재하지 않습니다.")
        else :
            print(f"{t.index(index)}번째 자료로 존재합니다.")
    else :
        print("잘못 입력하셨습니다. 다시 입력하세요.")