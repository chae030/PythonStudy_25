# 약수 구하기, 공약수 출력하기

num1 = int(input("첫번째 수 : "))
num2 = int(input("두번째 수 : "))
num1_divisor = set()
num2_divisor = set()

for i in range(1, num1+1) :
    if num1 % i == 0 :
        num1_divisor.add(i)
for i in range(1, num2+1) :
    if num2 % i == 0 :
        num2_divisor.add(i)

print(f"첫번째 수의 약수는 {num1_divisor}, 두번째 수의 약수는 {num2_divisor}")

print(f"{num1}과 {num2}의 공약수는 {num1_divisor&num2_divisor}")