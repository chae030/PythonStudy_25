# 신입생 입력 ~ 딕셔너리 연습

student = []
i = 0

while True :
    a = input("\n학생 정보 입력하기 (종료 q) ")

    if a == 'q' :
        print("프로그램을 종료합니다.")
        break
    
    else :
        info = {}

        info['학번'] = input('학번 : ')
        info['이름'] = input('이름 : ')
        info['생년월일'] = input('생년월일 : ')
        info['전화번호'] = input('전화번호 : ')
        info['주소'] = input('주소 : ')
        print(info)

        student.append(info)
        
        print(f"{i} 학생의 정보 입력 완료 : {info}")

        i = i + 1

print(f"\n전체 학생 정보\n{student}")