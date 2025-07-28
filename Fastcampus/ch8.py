f = open('New File', 'w')
f.write("hello python")
f.writelines(['list a', 'list b', 'c'])
f.close()

f = open('N file', 'w')
f.write("안뇽 방가방가~~ 개강이에요")
f.close()

f = open('N file', 'r')
print(f.read())
f.close()

try : 
    f = open('py.txt', 'r')
except :
    print('파일을 읽을 때 오류가 발생하였습니다.')

try : 
    f = open('python.py', 'r')
except FileNotFoundError: # catch랑 비슷한거
    print("파일을 찾을 수 없어염.... 파일을 만들지 않은 것 같아용")
else : # try 성공할경우
    a = f.read()
    print(a)
    f.close()
finally : # 무조건 실행됨
    print("못찾겠다잉")