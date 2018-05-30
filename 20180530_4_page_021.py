
score = eval(input("점수를 입력하세요. : "))

if score > 100:
    print("점수 입력이 잘못 됐습니다. - 100점 초과")
elif score >= 90:
    print("A 등급")
elif score >= 80:
    print("B 등급")
elif score >= 70:
    print("C 등급")
elif score >= 60:
    print("D 등급")
elif score >= 0:
    print("F 등급")
else :
    print("점수 입력이 잘못 됐습니다. - 0점 미만")
