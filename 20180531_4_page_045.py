import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("="*50)
print("■ 1부터 10까지 누적되는 합계를 출력하는 프로그램")
print("-"*50)
print(">>> 시작 카운트 변수의 값 = [ 1 ]")
print("-"*50)

sum = 0
for i in range(1,11):
    sum += i
    print("  --> 1부터 %02d까지 누적 합계 : %02d" %(i, sum))

print("-"*50)
print(">>> 카운트 변수의 값 = [%d]" %i)
print(">>> 1+2+...+9+10 = [%d]" %sum)
print("-"*50)
print("***프로그램을 종료합니다***")
print("="*50)
