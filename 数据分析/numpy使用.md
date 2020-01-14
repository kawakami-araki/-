Numpy 是python语言的一个扩展程序库,支持大量维度数组与矩阵运算,此外也针对数组运算提供大量的数学函数库

[TOC]

# 一、创建ndarray

## 1.使用np.array()创建

### 一维数组创建

- ```python
  import numpy as np
  array_1 = np.array([1,2,3])
  print(type(array_1))
  
  ```

  

### 二维数组创建

- ```python
  import numpy as np
  array_2 = np.array([[1,2,3],[1,2,3],[1,2,3]])
  print(type(array_2))
  ```

### 使用numpy模块的array方法,可以创建一维数组

- 同时,也可以空来创建二维数组

## 2.关于numpy 的一些用法

- ### linspace

  - 创建一个等差数列

  - ```python
    np.linspace(0, 100, num=35)
    linspace(start, stop, num )
    # num 为获取的数组的长度
    ```

- ### arange

  - 创建一个等差数列

  - ```python
    np.arange(0, 100, 20)
    # 第三个参数为每个数纸剑的差值
    ```

- ### random.randint

  - 随机创建多维数组

  - ```python
    np.random.randint(0, 100, size=(4,))
    np.random.randint(0, 100, size=(4, 10))
    np.random.randint(0, 100, size=(4, 10, 3))
    np.random.randint(0, 100, size=(4, 10, 3, 2))
    ```

  - 在randint中,第一个参数为随机数的最小值,第二个参数为随机数的最大值,size为数组的维度参数,具体表现形式为一个元组类型的数据,元组中只有一个数据为一维数组,两个为二维数组,以此类推

- random.seed

  - 固定随机性
  - 使用seed来使当前的随机状态固定下来,在seed不变的情况下,随机出来的数组将完全不会改变,除非修改了seed的参数,才会重新开始一次循环,否则seed将会记录下当前的数据状态,即使重新运行当前的python文件,也不会改变结果

- random.random

  - 创建一个0到1 的随机数数组

  - ```python
    print(np.random.random(size=(4)))
    print(np.random.random(size=(4, 10)))
    print(np.random.random(size=(4, 10, 3)))
    print(np.random.random(size=(4, 10, 3, 2)))
    ```

# 二、numpy数组属性

- ### ndim

  - 数组的维度,返回的结果为一个数字,对应数组的维度,一维数组为1

  - 使用方法:

    - ```python
      print(arr.shape)
      ```

- ### shape

  - 数组的形状(即为各维度的长度),返回的结果为数组各个维度的数值组成的元组

  - 使用方法:

    - ```python
      print(arr.ndim)
      ```

- ### dtype

  - 查看当前数组中的数据的类型

  - ```python
    print(arr.dtype)
    ```

- ### size

  - 查看当前数组的长度

  - ```python
    print(arr.size)
    ```

# 三、基本操作

- ### 索引

  - 无论是一维还是多维,索引与列表是相同的

- ### 切片

  - 无论是一维还是多维,切片与列表是相同的

  - 但是数组可以通过切片获取多维数组的前两列

  - 也即是说,每一个元素中只取前两个

  - ```python
    arr[1:4,:2,4:5]
    ```

  - 图片裁剪并保存

  - ```python
    plt.imsave('../photo/new4.jpeg', img_arr_1[:400,120:600,::-1])
    ```

- ### 变形

  - 将数组进行维度转义

  - ```python
    add = arr.reshape((40,))
    ```

  - 填充参数为一个元组类型的数据,可以将数组转译成符合参数概念的数组

  - 但是要注意的是,转义需要你精确的转移,也就是说,如果你的数组中只有20个元素,而你想转译成21个元素,就是不行的

- ### 级联

  - 对数组进行横向或者纵向的拼接

  - ```python
    
    img_arr_1 = plt.imread('../photo/困.jpeg')
    img_arr_2 = plt.imread('../photo/困.jpeg')
    new_img = np.concatenate((img_arr_1,img_arr_2), axis=0)
    new_img_1 = np.concatenate((new_img,new_img),axis=1)
    print(plt.imshow(new_img))
    plt.imsave('./new_img_1.jpeg', new_img_1)
    ```

  - 通过对图片数组的级联操作,我们可以实现图片的横向与纵向拼接

# 四、聚合操作

- ### sum

  - 求和

- ### max

  - 最大值

- ### min

  - 最小值

- ### mean

  - 平均值

- 进行运算时,参数axis可以不添加,当axis指定为0时,将会求出每一行的结果,当axis为1时,求出每一列的结果

# 五、排序操作

- sort
  - 通过axis来确定作用范围,当axis不指定的时候,将会默认进行全局排序,当axis=0的时候,进行行排序,当axis=1时,进行列排序
  - 使用sort时,np.sort并不会映射到原数据,arr.sort将会直接映射到原数据