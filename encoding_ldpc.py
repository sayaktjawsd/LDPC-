import random
x=[[0]*3]*200
y_para=[0]*100

for num in range(200):
    for n in range(3):
        x[num][n]=random.randint(0,99)
        if y_para[x[num][n]]==6:
            while y_para[x[num][n]]==6:
                x[num][n]=random.randint(0,99)
        y_para[x[num][n]]+=1
        print(x[num][n])

print('/n')



    


