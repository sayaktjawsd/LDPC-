import random
import os
x=[[0,0,0] for i in range(200)]
y_para=[0]*100
#count=[0]*100 #確認用

#行列の生成
for num in range(200):
    m=[-1,-1,-1]
    for n in range(3):
        x[num][n]=random.randint(0,99)
        if y_para[x[num][n]]==6 or x[num][n]==m[1] or x[num][n]==m[2]:
            while y_para[x[num][n]]==6 or x[num][n]==m[1] or x[num][n]==m[2]:
                x[num][n]=random.randint(0,99)
        y_para[x[num][n]]+=1
        m[n]=x[num][n]
'''
#テスト用
for m in x:
    for n in m:
        count[n]+=1
print(count)

file = os.path.abspath("test.txt")
with open(file, mode='w') as fp:
    for n in x:
        for m in n:
            fp.write(str(m))
            fp.write(' ')
'''
h=[[0 for i in range(200)] for j in range(100)]
for i, c in enumerate(x):
    for r in c:
        h[r][i]=1


file = os.path.abspath("test.txt")
with open(file, mode='w') as fp:
    for hh in h:
        for t in hh:
            fp.write(str(t))
            fp.write(' ')
        fp.write('\n')

        
        

