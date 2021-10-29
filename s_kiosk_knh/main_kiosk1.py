# CNU 버거 키오스크 프로그램
# 일자: 2021.10.29
# 작성자: 권남희
# 내용: Console 기반의 햄버거를 판매하는 키오스크 프로그램

import choice_menu

# 조건
# 사용자는 최대로 버거1개, 사이드1개, 음료1개 주문할 수 있습니다.

# 메뉴와 가격표
setmenu_name = {1: '상하이버거 세트', 2: '콰트로치즈버거 세트', 3: '트리플머쉬룸버거 세트'}
burger_name = {1: '상하이버거', 2: '콰트로치즈버거', 3: '트리플머쉬룸버거'}
side_name = {1: '치즈스틱', 2: '치킨너겟'}
drink_name = {1: '코카콜라', 2: '커피', 3: '주스'}

setmenu_price = {1: 5000, 2: 7000, 3: 8000}
burger_price = {1: 3000, 2: 3500, 3: 4000}
side_price = {1: 1500, 2: 2000}
drink_price = {1: 1000, 2: 1200, 3: 1500}


# 고객 주문 기록 저장
menu_save = {}   # 고객 주문 메뉴 기록
price_save = {}  # 고객 주문 금액 기록

while True:

    ####################
    ## 1.메인 메뉴 선택 ##
    ####################
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ == CNU 버거(ver.01) ==')
    print('■■ CNU 버거에 방문해주셔서 감사합니다.')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ 메뉴')
    print('□■ 1.햄버거 세트') # 햄버거, 사이드, 음료
    print('□■ 2.햄버거 단품') # 햄버거
    print('□■ 3.사이드 메뉴') # 사이드
    print('□■ 4.음료')       # 음료
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

    while True:
        print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
        menu_num = int(input('>> 번호:'))     # 사용자부터 주문 MENU 입력

        if menu_num >= 1 and menu_num <= 4:  # 사용자가 정상적인 값 입력
            break
        else:
            print('# MSG: 1~4의 번호만 입력해주세요 :)')

    ###################
    ## 2.세부메뉴 선택 ##
    ###################
    if menu_num == 1:    # 햄버거 세트
        # 햄버거 세트 메뉴 선택(햄버거 세트에 따라 햄버거 종류 결정)
        choice_num = choice_menu.choice_setmenu()  # choice_menu.py에서 choice_setmenu() 함수를 호출하세요.
        menu_save['setmenu'] = setmenu_name[choice_num]
        price_save['setmenu'] = setmenu_price[choice_num]

        # 사이드 단품 세부 메뉴 선택
        choice_num2 = choice_menu.choice_side()
        menu_save['side'] = side_name[choice_num2]
        price_save['side'] = side_price[choice_num2]

        # 음료 단품 세부 메뉴 선택
        choice_num3 = choice_menu.choice_drink()
        menu_save['drink'] = drink_name[choice_num3]
        price_save['drink'] = drink_price[choice_num3]

    elif menu_num == 2:
        choice_num1 = choice_menu.choice_burger()  # choice_menu.py에서 choice_burger() 함수를 호출하세요.
        menu_save['burger'] = burger_name[choice_num1]
        price_save['burger'] = burger_price[choice_num1]

    elif menu_num == 3:
        choice_num2 = choice_menu.choice_side()    # choice_menu.py에서 choice_side() 함수를 호출하세요.
        menu_save['side'] = side_name[choice_num2]
        price_save['side'] = side_price[choice_num2]

    elif menu_num == 4:
        choice_num3 = choice_menu.choice_drink()   # choice_menu.py에서 choice_drink() 함수를 호출하세요.
        menu_save['drink'] = drink_name[choice_num3]
        price_save['drink'] = drink_price[choice_num3]

    # 고객 주문 완료
    print(menu_save)
    print(price_save)


    ##################################
    ## 3.주문 메뉴와 금액 정산 및 출력 ##
    ##################################

    # Total 주문 금액 계산
    total_price = 0  # Total 주문 금액

    for price in price_save.values():
        total_price += price

    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 고객님이 주문하신 메뉴는 ')
    for i, menu in enumerate(menu_save.values()):
        print('□■ {}. {}'.format(i+1, menu))
    print('■■ (으)로 총 주문금액은 {}원 입니다.'.format(total_price))
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 주문 완료! 이용해주셔서 감사합니다. 또 방문해주세요 :)')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    menu_save = {}
    price_save = {}

    # 조건: 프로그램 종료전까지 계속 동작하도록 만들어주세요.
    while True:
        a = input('■■ 키오스크 프로그램을 종료하시겠습니까? yes 또는 no로 대답해주세요 :):')
        if a == 'yes':
            print('■■ 이용해주셔서 감사합니다. 프로그램 종료하겠습니다!')
            break
        elif a == 'no':
            break
        else:
            print('# MSG: yes 또는 no로만 입력해주세요 :)')
    if a == 'yes':
        break