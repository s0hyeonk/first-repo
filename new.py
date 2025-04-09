menu = input("점메추 해드립니다. 원하는 분야를 알려주세요 (한식/양식/일식/중식) :")
spic = int(input("맵기를 선택해주세요(1~5) :")) 
if menu == "한식" :
    if spic == 1 :
        print("설렁탕/ 곰탕/ 불고기덮밥/ 미역국/ 잡채/ 잔치국수/ 물냉면 / 생선구이/ 백숙")
    elif spic == 2 :
        print("비빔밥/ 된장찌개/ 도토리묵/ 칼국수/ 열무국수/ 샤브샤브/ 제육볶음 ")
    elif spic == 3 :
        print("김치찌개/ 감자탕/ 해장국/ 김치전/ 육개장/ 부대찌개 ")
    elif spic == 4 :
        print("떡볶이/ 매운탕 ")
    elif spic == 5 :
        print("불닭볶음면/ 닭발/ 실비김치 ")
    else :
        print("맵기를 다시 선택하라")
if menu == "양식" :
    if spic == 1 :
        print("크림파스타/ 고르곤졸라피자/ 돈가스/ 양송이(크림)스프/ ")
    elif spic == 2 :
        print("스파게티/ 페퍼로니피자 ")
    elif spic == 3 :
        print("칠면조")
    elif spic == 4 :
        print("존재하지않음")
    elif spic == 5 :
        print("존재하지않음")
    else :
        print("맵기를 다시 선택하라")
if menu == "일식" :
    if spic == 1 :
        print("푸딩/ 낫또 ")
    elif spic == 2 :
        print("스시/ 라멘")
    elif spic == 3 :
        print("몰라")
    elif spic == 4 :
        print("몰라")
    elif spic == 5 :
        print("몰라")
    else :
        print("맵기를 다시 선택하라")