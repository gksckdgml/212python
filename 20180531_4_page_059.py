import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

cnt = 0
sum = 0

#number = int(input(">> 어디까지 구할까요? :  "))
number = 10

print("-" * 55)

while cnt < number :
    cnt += 1
    if cnt % 2 != 0 :
        continue
    else :
        sum += cnt
        print(">> 2 부터 %3d 까지 짝수의 누적합 ... %5d" % (cnt, sum))
