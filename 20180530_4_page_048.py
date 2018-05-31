import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("="*50)
print("■ 1부터 키보드로 입력받은 수까지 짝수의 누적합계 출력")
print("-"*50)
#input = int(eval(input(">>> 어디까지 입력할까요? : ")))
input = 10000

i = 0
sum = 0

while i <= input:
    sum += i
    i += 2

print(">>> 카운트 변수의 현재값 : ", i)
print("-"*50)
print(">>> 1부터 ",input, "까지 짝수의 누적 합계 : ", sum)
print("-"*50)
print("프로그램을 종료합니다")
