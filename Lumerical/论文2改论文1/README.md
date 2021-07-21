### 改进项目说明文件

#### 1、`Phix.xlsx`、`Phiy.xlsx`、`rlPhix.xlsx`、`rlPhiy.xlsx`

改进结构中每个位置硅柱所需的相位。

#### 2、`Phi.xlsx`

小组扫描单个结构得到的数据库。

#### 3、`Find_3.py`

Python程序实现从`Phi.xlsx`中找到与`Phix.xlsx`和`Phiy.xlsx`最接近的结构尺寸并输出到`Rect.xlsx`。(以垂直与水平结构为例，其他两个结构方法相似)

#### 4、`Rectxy.lsf`、`Rectab.lsf`、`Rectrl.lsf`

利用输出的尺寸实现结构的排列，并添加衬底，监视器等其他结构。三种结构分别为“H/V”、“±45°”、“RHCP/LHCP”。

#### 5、`x.fsp`、`y.fsp`、`a.fsp`、`b.fsp`、`r.fsp`、`l.fsp`

仿真的六个结构单元

