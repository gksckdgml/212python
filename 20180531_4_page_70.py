import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

palse = [165,123,149,108,93]
cnt = 0

for blood in palse:
    cnt += 1
    if blood >= 140:
        print(cnt, " 고혈압 : ", blood)
    elif 120 <= blood < 140:
        print(cnt, " 정상혈압 : ", blood)
    else:
        print(cnt, " 저혈압 : ", blood)
        
