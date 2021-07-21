# 寻找最佳矩形柱长宽Python程序。
# 目标相位为"Phix.xlsx"和"Phiy.xlsx"。扫描得到的数据为"Phi.xlsx"。
# 程序执行结果保存在"Rect.xlsx"
# %% 导入Python程序依赖包
import pandas as pd
import numpy as np
# %% 读取数据
x0 = pd.read_excel('Phix.xlsx')
y0 = pd.read_excel('Phiy.xlsx')
phix = pd.read_excel('Phi.xlsx')
phix = np.array(phix)
x0 = np.array(x0)
y0 = np.array(y0)
phiy = phix.T
# %% 遍历目标相位，在扫描相位中找最接近的尺寸输出
data = []
a = []
b = []

for w in range(5):
    for z in range(20):
        FoM = np.zeros((51, 51))
        for m in range(51):
            for n in range(51):
                FoM[m, n] = abs(phix[m, n]-x0[w, z])+abs(phiy[m, n]-y0[w, z])
# minnum = min(min(num) for num in FoM)

        min = FoM[0][0]

        p = 0
        q = 0
        for x in range(51):
            for y in range(51):
                if FoM[x, y] < min:
                    p = x
                    q = y
                    min = FoM[x, y]
        a.append(p)
        b.append(q)
        data.append(min)
# %% 保存执行结果到"Rect.xlsx"
xl = np.array(b)
x0length = (xl)*0.01+0.1
yl = np.array(a)
y0length = (yl)*0.01+0.1
doc = pd.DataFrame([data, x0length, y0length]).T
doc.columns = ['min', 'RECTxength', 'RECTyength']
doc.to_excel('Rect.xlsx')
