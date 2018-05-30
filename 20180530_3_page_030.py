import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

with open("D:/Python_ex/pathfile.txt", "a") as fileName :
    data = "\n---<< 추가 내용 2 >>---\n"
    fileName.write(data)

    for cnt in range(16, 21) :
        addWrite = " +++> %02d 회 동계올림픽 \n" % cnt
        fileName.write(addWrite)

"""
filename = open("d:/Python_ex/pathfile.txt", "a")
for i in range(11, 16):
    prt = " ===> %02d 회 동계올림픽 \n" % i
    filename.write(prt)

filename.close()
---
filename = open("d:/Python_ex/pathfile.txt", "r")
all_data = filename.readlines()
for i in all_data:
    print(i)
---
filename = open("d:/Python_ex/pathfile.txt", "w")
for i in range(1, 11):
    prt = " ---> %02d 회 동계올림픽 \n" % i
    filename.write(prt)
filename.close()
"""
