[TOC]



# redis数据库安装与使用:

- 前往github下载要使用的版本的压缩包
- 解压缩文件
- cd到安装目录
- 运行redis-server
- 将安装目录添加到系统环境变量中
- 运行redis-server
- 再次打开一个cmd窗口,输入redis-cli即可进入redis环境
- keys *   查看当前所有数据
- 端口: 127.0.0.1:6379

## redis数据类型:

- list
  - llen
    - 获取列表长度
  - lpush
    - 在表头添加数据
  - rpush
    - 在表尾添加数据
  - lpop 
    - 从表头弹出数据
  - rpop
    - 从表尾弹出数据
  - rpoplpush
    - 从表尾弹出数据并添加到表头
  - lrange listName num num  
    - 从xx到xx的所有数据,支持负数
  - lindex listName num
    - 指定下标获取对应的值
  - linsert key    (before) value newvalue
    - 在某个值之前添加另一个新的数值
  - linsert key    (after) value newvalue
    - 在某个值之后添加另一个新的值
  - lrem key  n  value 
    - 删除某个值,n为次数
    - 当n > 0,则删除n个对应的值,且删除顺序从左往右
    - 当n < 0,删除n个对应的值,且删除顺序从右往左
    - 当n = 0,则删除所有符合条件的数据
- string
  - 二进制安全的键值对,以key:value的形式存在,也就是说,可以存储二进制文件
  - string单个大小最大为512M
- set
  - set设定键值对
  - get根据键获取对应的值
  - append 在键对应的值后面追加新的数据,同时具备set的概念,如果追加的目标是一个不存在的键,将会自动创建出来
  - strlen 获取键对应的字符串的长度
  - setnx 对一个键进行赋值,如果该键存在,则不会有任何效果,如果该键并不存在,则进行创建并赋值
  - incr 对键对应的值进行+1操作,前提是这个值是纯粹的数字
  - decr 对键对应的值进行-1操作,前提是这个值不是纯数字
  - incrby keysName num 对键所对应的值进行加法操作,
  - decrby  keysName num 对键所对应的值进行减法操作
- hash
- zset

## redis基础操作:

- keys * 
  - 查看所有的数据
- exists name
  - 查看符合该名称的数据总量
- del name
  - 删除目标数据
- expire name succes
  - 为一个数据设置过期时间,时间单位默认为秒,需输入数字
- ttl name
  - 查看该对象还有多久过期
- dbsize
  - 查看当前正在使用的库中的数据的数量
- Flushdb
  - 清空当前的库
- Flushall
  - 清空所有的库