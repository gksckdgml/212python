import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("-"*50)
print("티켓 구입가능 여부 확인")
print("결재방법은 다음과 같습니다.")
print("-"*50)
print("a.현  급 결재시 cash 입력하세요.")
print("b.카  드 결재시 card 입력하세요.")
print("c.핸드폰 결재시 phone 입력하세요.")
print("-"*50)

ticket = ["cash", "card", "phone"]

c_value = input("--> 결재 방법을 입력하세요 : ")

if c_value in ticket:
    print(">>> [%6s] 결재 방법을 선택하셨습니다." %c_value)
    print("티켓 구매가 가능합니다.")
else:
    print(">>> [%6s]은(는) 유효한 결재 방법이 아닙니다." %c_value)
    print("다시 선택해 주시기 바랍니다.")

print("-"*50)
