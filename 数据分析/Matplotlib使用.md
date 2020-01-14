---
Matplotlib 使用了一些numpy的功能,但是其主要功能在于对图片的操作
---

 

[TOC]

# 一、Matplotlib

## 	使用Matplotlib对numpy数组进行操作,该数组来源于一张图片

# 二、实例

## (一)对猫咪的图片进行相关操作

#### 1.具体实现的代码块

```python
import matplotlib.pylab as plt
# 导入对图片处理的模块
img_arr_1 = plt.imread('../photo/困.jpeg')
# 使用imread对图片以数组的形式进行读取
img_arr_2 = plt.imread('../photo/困.jpeg')
# 多个数组之间可以进行拼接
img_arr_3 = (img_arr_1 + img_arr_2) * 2
# 在对图片数组进行直接性加值的时候,需要注意,运算之后的数据不能大于255,否则将会报错
# ValueError: Image RGB array must be uint8 or floating point; found uint16
# 如上述代码出现,则意味着加值过高,长处rgb颜色的范围,需要将数值修改
plt.imsave('../photo/new.jpeg', img_arr_3 + 100)
```

#### 2.详细的图片处理方法

(1)imread

- 以数组的形式读取图片信息
- imread(filePath)

(2)imsave

- 将数组形式的图片信息保存起来
- imsave(filename, fileArray)

(3)imshow

- 将图片数组以图片的形式展示
- imshow(fileArray)