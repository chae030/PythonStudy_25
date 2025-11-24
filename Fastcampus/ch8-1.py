# 생일 찾기 프로그램
# 변형 : 저장소에 없으면 새로 저장

def findbirth() :
    name_birth = {'alex' : '2024.07.24'}
    while True :
        name = input("\n생일을 알고 싶은 사람을 입력하세요 (종료 X): ")
        if name == 'X' or name == 'x' :
            print("프로그램을 종료합니다.\n")
            break
        elif name in name_birth :
            print(f"{name}의 생일은 {name_birth[name]} 입니다.")
        else : 
            while True :
                empty = input("저장소에 없습니다. 새로 저장하시겠습니까? (Y/N) : ")
                if empty == 'Y' or empty == 'y':
                    name_birth[name] = input(f"{name}의 생일 : ")
                    print("저장되었습니다. 초기 화면으로 돌아갑니다.")
                    break
                elif empty == 'N' or empty == 'n':
                    print("초기 화면으로 돌아갑니다.")
                    break
                else :
                    print("잘못 입력하셨습니다.")

findbirth()
