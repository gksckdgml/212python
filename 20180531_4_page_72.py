import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

kk = 1
for i in range(1,4):
    for j in range(1,10):
        for k in range(kk,kk+3):
            print("%2d x %2d = %2d     " %(i+k,j,(i+k)*j), end="")
        print("")
    print("-"*50)
    kk += 2
