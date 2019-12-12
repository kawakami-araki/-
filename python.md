# 使用vscode写django文件时遇到的一点小小的问题,记录一下

在创建django项目时,出现了报错提示,上面显示,数据库模型对象没有objects对象

针对于此,特地查了一下,找到了解决方法

```
"python.linting.pylintArgs": [
        "--load-plugins=pylint_django"
    ]
```

在项目下出现的.vscode文件夹中,找到setting.json文件,并在其中加入这串代码

如果没用,使用pip命令,下载pylint-django