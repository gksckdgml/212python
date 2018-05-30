import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("*** 디렉터리에 새 파일 생성하기 프로그램 ***")
print("-" * 50)
print("-- 생성할 파일명 : pathfile.txt --")
print("-" * 50)

filename = open("d:/Python_ex/pathfile.txt", "w")

for i in range(1, 11) :
    prt = " ---> %02d 회 동계올림픽 \n" % i
    filename.write(prt)

filename.close()

print("\n*** 파일 생성 완료 ***\n")
