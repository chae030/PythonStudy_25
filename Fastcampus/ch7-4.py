# 카드게임

card_n = list(range(2, 11))
card_n.extend(['J', 'Q', 'K'])
card_n.insert(0, 'A')
card_s = ['♠', '♥', '♣️', '◆']

print(card_n, card_s)

card = set()
for i in card_n :
    for j in card_s :
        card.add(str(i)+j)

while True :
    a = input("엔터키를 누르면 카드가 나옵니다. 'q'를 누르면 종료합니다. ")
    if a == 'q' :
        print("프로그램을 종료합니다.")
        break
    print(f"이번에 나온 카드는 {card.pop()} 입니다.")

