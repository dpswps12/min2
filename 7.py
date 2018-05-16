engkor_dict = dict()
while True:
    eng = input("영어 단어 : ")
    if len(engkor_dict) <= 0:
        print("사전이 비어 있습니다.")
    elif eng == "":
        break
    elif eng in engkor_dict:
        print(eng, ':', kor)
        continue
    elif len(engkor_dict) > 0:
        print(eng, "단어가 등록되어 있지 않습니다.")
    print("단어를 추가 합니다.")
    kor = input("한글 단어 : ")
    engkor_dict[eng] = kor
print(engkor_dict)


