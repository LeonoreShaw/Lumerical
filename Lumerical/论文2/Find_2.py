## Python实现论文2结构尺寸的查找
#Phi1.xlsx和Phi2.xlsx为需要的相位，Phi.xlsx为数据库，输出保存在xyLen.xlsx文件中。
# %%
from numpy.lib.function_base import append
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator ,FormatStrFormatter
from tkinter import _flatten
# %%
x0=pd.read_excel('Phi1.xlsx')
y0=pd.read_excel('Phi2.xlsx')
phix=pd.read_excel('Phi.xlsx')
phix=np.array(phix)
x0=np.array(x0)
y0=np.array(y0)
phiy=phix.T
# %%
data=[]
a=[]
b=[]

for w in range(5):
    for z in range(20):
        FoM = np.zeros((61, 61))
        for m in range(61):
            for n in range(61):
                FoM[m,n]=abs(phix[m,n]-x0[w,z])+abs(phiy[m,n]-y0[w,z])
# minnum = min(min(num) for num in FoM)



        min=FoM[0][0]

        p=0
        q=0
        for x in range(61):
            for y in range(61):
                if FoM[x,y]<min:
                    p=x
                    q=y
                    min=FoM[x,y]
        a.append(p)
        b.append(q)
        data.append(min)
# %%
xl=np.array(a)
x0length=(xl)*0.005+0.05
yl=np.array(b)
y0length=(yl)*0.005+0.05
doc=pd.DataFrame([data,x0length,y0length]).T
doc.columns = ['min','x0length','y0length']
doc.to_excel('DxDy.xlsx')

