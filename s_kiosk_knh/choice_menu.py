# 0. 세트 메뉴 선택하는 함수
def choice_setmenu():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■  SET MENU')
    print('□■  1.상하이버거 세트: 5,000원')
    print('□■  2.콰트로치즈버거 세트: 7,000원')
    print('□■  3.트리플머쉬룸버거 세트: 8,000원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')

    while True:
        choice_num = int(input('>> 번호: '))
        if choice_num >= 1 and choice_num <= 3:
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요 :)')
    return choice_num


# 1. 햄버거 세부 메뉴 선택하는 함수
def choice_burger():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■  BURGER MENU')
    print('□■  1.상하이버거: 3,000원')
    print('□■  2.콰트로치즈버거: 3,500원')
    print('□■  3.트리플머쉬룸버거: 4,000원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')

    while True:
        choice_num1 = int(input('>> 번호: '))
        if choice_num1 >= 1 and choice_num1 <= 3:
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요 :)')
    return choice_num1


# 2. 사이드 세부 메뉴 선택하는 함수
def choice_side():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■  SIDE MENU')
    print('□■  1.치즈스틱: 1,500원')
    print('□■  2.치킨너겟: 2,000원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    while True:
        choice_num2 = int(input('>> 번호: '))
        if choice_num2 >= 1 and choice_num2 <= 2:
            break
        else:
            print('# MSG: 1~2의 번호만 입력해주세요 :)')
    return choice_num2

# 3. 음료 세부 메뉴 선택하는 함수
def choice_drink():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■  DRINK MENU')
    print('□■  1.코카콜라: 1,000원')
    print('□■  2.커피: 1,200원')
    print('□■  3.주스: 1,500원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

    while True:
        choice_num3 = int(input('>> 번호: '))
        if choice_num3>= 1 and choice_num3 <= 3:
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요 :)')
    return choice_num3