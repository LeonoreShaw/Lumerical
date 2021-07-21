## Python实现两个Excel间的数据查找
#data1.xlsx为遍历数据，data2.xlsx为扫描数据库
#程序执行结果保存在DxDy.xlsx文件中
# %%
import pandas as pd
import numpy as np

data1=pd.read_excel('data1.xlsx')
data2=pd.read_excel('data2.xlsx')
# %%
data1=np.array(data1)
data2=np.array(data2)
# %%
data1=np.reshape(data1,[121,1])
data1=data1.tolist()
# %%
m=data2.shape[0]
n=data2.shape[1]
# %%
data=[]
a=[]
b=[]
fai=[0 for _ in range(121)]
ji=0
for item in data1:
    p=0
    q=0
    l=np.abs(data2[p][q]-item)
    fai[ji]=data2[p][q]
    for x in range(m):
        for y in range(n):
            distance=np.abs(data2[x][y]-item)
            if distance<l:
                p=x
                q=y
                l=distance
                fai[ji]=data2[x][y]
    ji=ji+1
    a.append(p)
    b.append(q)
    data.append(item)
# %%
dx=np.array(a)
dx=(dx+10)/100
dy=np.array(b)
dy=(dy+10)/100
doc=pd.DataFrame([data,fai,dx,dy]).T
doc.columns = ['data1','data2','Dx','Dy']
doc.to_excel('DxDy.xlsx')