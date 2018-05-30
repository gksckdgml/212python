blood_data = {"a":"A형-차분한 성격","b":"B형-발전적 성격","o":"O형-활발한 성격","ab":"AB형-도전적성경"}

c_input = input("혈액형을 입력하세요.(입력값 : a/b/o/ab) :")
c_input = c_input.lower()

if c_input in blood_data:
    print(blood_data.get(c_input))
else:
    print("입력값 오류 : a/b/o/ab 중에 하나를 입력해 주세요.")
