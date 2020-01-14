---

---

[TOC]

# Pandas的数据结构

```python
import pandas as pd
from pandas import Series,DataFrame
```



## 一、Series

#### 1.Series时一种类似于一维数组的对象,主要由以下两个部分 组成:

- values:一组数据
- index: 相关的数据索引标签

#### 2.Series创建方式

1. ##### 由列表

   使用列表创建

   - ```python
     # 创建一个对象,该对象不指定索引,将会默认使用0---(n-1)的形式
     import pandas as pd
     from pandas import Series,DataFrame
     a_ser = Series(data=[1,2,3,4])
     print(a_ser)
     print(a_ser['a'])
     ```

   - ```python
     # 创建指定索引的对象,该对象的索引可以自行指定
     # 显示索引的存在并不影响正常索引的使用
     # 此种索引的形式被称之为   显示索引
     import pandas as pd
     from pandas import Series,DataFrame
     a_ser = Series(data=[1,2,3,4], index=['a', 'b', 'c', 'd'])
     print(a_ser)
     print(a_ser['a'])
     ```

2. ##### 使用numpy数组创建

   使用数组创建

   - ```python
     # 隐式索引
     import pandas as pd
     from pandas import Series,DataFrame
     import numpy as np
     b_ser = Series(data=np.random.randint(0,100,size=(5,)))
     print(b_ser)
     ```

   - ```python
     # 显示索引
     import pandas as pd
     from pandas import Series,DataFrame
     a_ser = Series(data=[1,2,3,4])
     import numpy as np
     b_ser = Series(data=np.random.randint(0,100,size=(5,)), index=['a', 'b', 'c', 'd', 'e'])
     print(b_ser)
     ```

## 二、切片

### 	显示索引切片与隐式索引切片

- ```python
  print(a_ser[0:3])
  ```

## 三、series基本概念

1. 可以将Series看作是一个定长的有序字典

2. 使用size,shape,index,values获取对应的属性

   - ```python
     a_ser.size     # 元素的长度
     a_ser.shape    # 对象的形状
     a_ser.values   # 对象的内容,也就是这个对象中储存的所有内容
     a_ser.index    # 对象的索引,如果有显示索引的话返回显示索引,没有的话显示隐式索引
     ```

3. 使用head和tail获取前n个数或者后n个数

   - ```python
     print(b_ser.head(2))
     ```

   - ```python
     print(b_ser.tail(2))
     ```

4. 对Series进行去重

   - ```python
     print(b_ser.unique())
     ```

5. 对两个Series进行相加

   - ```python
     s = a_ser + b_ser
     print(s)
     # 在执行加法运算的时候,将会把对应索引位置的数值相加
     # 如果其中一个的数值不存在,那么这个位置的数值将会变成null, 也就是显示出来的NaN
     ```

6. 关于是否为空的判定

   - ```python
     print(s.isnull()) 
     print(s.notnull())
     ```

7. 基于空值判定的结果进行取值

   - ```python
     print(s[[1,2]])
     # 正常的下标取值,可同时取多个值
     print(s[[True, True, True, False, False]])
     # 通过布尔值进行取值,将会根据对应位置的布尔值进行取值,当为True时将会把值取出来,否则不取
     print(s[s.notnull()])
     # 根据空值判断结果进行取值,取出不为空的数值
     print(s[s.isnull()])
     # 根据控制判断结果进行取值,取出为空的数值
     ```

8. 

