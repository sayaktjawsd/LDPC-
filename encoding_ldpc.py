import random
import os
import numpy as np

def mat_fprint(h):
    #行列をファイル出力
    file = os.path.abspath('test.txt')
    with open(file, mode='w') as fp:
        for hh in h:
            for t in hh:
                fp.write(str(t))
                fp.write(' ')
            fp.write('\n')




#行列を生成する
def mat_gene(row,column):
    x=[[0,0,0] for i in range(column)]
    y_para=[0 for i in range(row)]
    #count=[0]*100 #確認用
    for num in range(column):
        m=[-1,-1,-1]
        for n in range(3):
            x[num][n]=random.randint(0,row-1)
            if y_para[x[num][n]]==6 or x[num][n]==m[0] or x[num][n]==m[1]:
                while y_para[x[num][n]]==6 or x[num][n]==m[0] or x[num][n]==m[1]:
                    x[num][n]=random.randint(0,row-1)
            y_para[x[num][n]]+=1
            m[n]=x[num][n]
    
    h=[[0 for i in range(column)] for j in range(row)]
    for i, c in enumerate(x):
        for r in c:
            h[r][i]=1
    return h

 
#Hに関する前処理 
def extend(n,k,t,g,mat_h):
    print('ext')
    print(t)
    print(g)

    dig_mat=np.count_nonzero(mat_h[t:n-k-g]==1,axis=0)
    print(dig_mat)

    for s in range(n):
        if dig_mat[s]==1:
            c=s #extendで選んだ列の添え字
            break
    print(c)

    l = mat_h[t:n-k-g,c].tolist()
    r=l.index(1)
    r+=t
    print(r)
    print(c)
    #swap
    mat_save=mat_h[:,c].tolist()
    mat_h[:,c]=mat_h[:,t]
    mat_h[:,t]=np.array(mat_save)
    print(mat_h)
  

    mat_save=mat_h[r].tolist()
    mat_h[r]=mat_h[t]
    mat_h[t]=np.array(mat_save)
    
    return mat_h


def choose(n,k,t,g,mat_h):
    print('cho')
    dig_mat=np.count_nonzero(mat_h[t:(n-k-g)]==1,axis=0)
    dig_mat=dig_mat.tolist()

    c=dig_mat.index(min(dig_mat))

    print('dig_mat')
    print(dig_mat)
    print('t')
    print(t)

    r_ind=[]
    col_c=mat_h[:,c+t].tolist()
    
    for i,s in enumerate(col_c):
        if s==1:
            r_ind.append(i)
    d=len(r_ind)
    print('r_ind')
    print(r_ind)

    #Swap
    mat_save=mat_h[:,c+t].tolist()
    mat_h[:,c+t]=mat_h[:,t]
    mat_h[:,t]=np.array(mat_save)

    dig_mat=np.count_nonzero(mat_h[t:(n-k-g)]==1,axis=0)
    dig_mat=dig_mat.tolist()
    print('dig_mat')
    print(dig_mat)

    mat_save=mat_h[r_ind[0]].tolist()
    mat_h[r_ind[0]]=mat_h[t]
    mat_h[t]=np.array(mat_save)
    btm_mat=[]

    dig_mat=np.count_nonzero(mat_h[t:(n-k-g)]==1,axis=0)
    dig_mat=dig_mat.tolist()
    print(dig_mat)

    print(r_ind)
    
    print(mat_h.shape)
    
    for i in r_ind[1:]:
        btm_mat.append(mat_h[i].tolist())

    print(btm_mat)

    mat_h=np.delete(mat_h,r_ind[1:],0)

    mat_h=np.append(mat_h,np.array(btm_mat),axis=0)

    print(mat_h.shape)
    
    dig_mat=np.count_nonzero(mat_h[t:(n-k-g)]==1,axis=0)
    dig_mat=dig_mat.tolist()
    print(dig_mat)
    
    
    g+=d-1
    return g,mat_h

#前処理の本体関数
def preprocess(h0,n,k):
    t = 0 
    g = 0
    mr_deg=3 #the minimum residual degree
    #mr_degを計算する
    
    while t!=n-k-g:
        if mr_deg==1:
            h0 = extend(n,k,t,g,h0)
            t+=1
            print(t)
            #mr_degの計算
            dig_mat=np.count_nonzero(h0[t:n-k-g]==1,axis=0)
            dig_mat=dig_mat.tolist()
            #forbunn回して０いがいのminを探す
            mr_deg=3
            for i,s in enumerate(dig_mat):
                if s!=0:
                    if s<mr_deg:
                        mr_deg=s

            print(dig_mat)
            print('me_deg')
            print(mr_deg)
            print(h0)
            
        else:
            l=choose(n,k,t,g,h0)
            g=l[0]
            #mr_deg=3-g
            t+=1
            h0=l[1]
            #mr_degの計算
            print('h0真ん中')
            print(h0[t:n-k-g])
            dig_mat=np.count_nonzero(h0[t:n-k-g]==1,axis=0)
            dig_mat=dig_mat.tolist()
            mr_deg=3
            for i,s in enumerate(dig_mat):
                if s!=0:
                    if s<mr_deg:
                        mr_deg=s
            print(dig_mat)
            print('me_deg')
            print(mr_deg)

            print(h0)
            print(t)
            print(g)
    return h0,g

#main
h0=mat_gene(100,200)
'''
h0=[[0,0,1,1,0,1,0,1,0,1,1,0],
    [1,0,0,1,0,1,1,0,1,0,1,0],
    [0,1,1,0,0,1,1,1,0,0,0,1],
    [0,1,1,0,1,0,1,0,1,1,0,0],
    [1,0,0,1,1,0,0,1,1,0,0,1],
    [1,1,0,0,1,0,0,0,0,1,1,1]]
'''
h0=np.array(h0)
#dig_mat=np.count_nonzero(h0==1,axis=0)
#print(dig_mat)
'''
h= [[1,1,0,0,0,1,1,0,1,0,1,0],
    [0,1,1,1,0,0,1,1,0,0,1,0],
    [0,0,1,1,1,1,0,0,1,1,0,0],
    [0,0,0,1,0,1,1,1,0,1,0,1],
    [1,1,0,0,1,0,0,1,1,0,0,1],
    [1,0,1,0,1,0,0,0,0,1,1,1]]
h=np.array(h)
'''


ph=preprocess(h0,200,100)
h=ph[0]
g=ph[1]
mat_fprint(h)
print('g')
print(g)
#mat_fprint(h)
'''
check=[[1,0,0,0,0,0],
        [0,1,0,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,1,0,0],
        [1,1,0,0,1,0],
        [1,1,1,0,0,1]]
check=np.array(check)
print(np.dot(check,h2))
'''
s=[0 for num in range(100)]
for i in range(30):
    s[3*i]=1
s=np.array(s)
n=200
k=100

#encoding
mat_t=h[0:n-k-g,0:n-k-g]
mat_a=h[0:n-k-g,n-k-g:n-k]
mat_b=h[0:n-k-g,n-k:n]

mat_e=h[n-k-g:n-k,0:n-k-g]
mat_c=h[n-k-g:n-k,n-k-g:n-k]
mat_d=h[n-k-g:n-k,n-k:n]

p2_1=np.dot(mat_b,s.T)
p2_1=p2_1 % 2
inv_t=np.linalg.inv(mat_t)%2
inv_t=np.array(inv_t,dtype='int8')
p2_1=np.dot(inv_t,p2_1)%2

p2_1=np.dot(mat_e,p2_1)%2
p2_2=np.dot(mat_d,s.T)%2

p2=(p2_1+p2_2)%2
fi_1=np.dot(mat_e,inv_t)%2
fi_1=np.dot(fi_1,mat_a)%2
fi=(mat_c+fi_1)%2

fi=np.linalg.inv(fi)
p2=np.dot(fi,p2)%2
p2=np.array(p2,dtype='int8')

p1_1=np.dot(mat_a,p2.T)%2
p1_2=np.dot(mat_b,s.T)%2
p1=(p1_1+p1_2)%2
p1=np.dot(np.linalg.inv(mat_t)%2,p1)
p1=np.array(p1%2,dtype='int8')

print('p1: ')
print(p1)
print('p2: ')
print(p2)
print('s: ')
print(s)


'''
#count=[0]*100 #確認用
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



        
        

