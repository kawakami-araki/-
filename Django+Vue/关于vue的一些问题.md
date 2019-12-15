## 第一点

​	最初老师教的其实是2.0版本,相比起来,更加高端的vue/cli3的代码更加简洁高效,我也不知道为啥学校不叫最新的,反正当初这个坑是被我踩到了

​	这其中有着很多的问题,如缺少依赖包,缺少必备的代码库,林林总总的红色报错在当时直接把我惊呆了

​	因为在出问题之前,我一直是在使用webstorm进行代码的编写,webstorm是个很好的软件,基本上,只要你装好了环境,他就能帮你进行一系列的操作,但也正是这些,导致我压根没发现这些潜在的问题

​	事情的起因,是因为我的webstorm到期了......![1576150667489](C:\Users\lenovo\Desktop\-\Django+Vue\assets\1576150667489.png)

​	这是一个悲伤的故事,我的电脑中安装了很多编辑器

​	包括webstorm,pycharm,codeblock,vscode,golang等等,也正是因为到期了,我便决定收拾一下vscode,将vue问价你放到vscode中去写

​	然后问题就出现了.

先是新建的vue文件无法显示,然后就是疯狂报错,到最后,我三个dos窗口全是红色,惨不忍睹

于是忍痛删掉了电脑中的vue插件,然后开始重新安装

以下是这两天安装的全部插件,不排除被我忘记的可能

- npm install @vue/cli -g –save

- npm install axios

- npm install stylus

- npm install stylus-loader

- npm install style-loader

- npm install css-loader

- npm install pug

- npm install webpack

- npm install cors-js

- ps:更多的插件一时想不起来了.反正,凡是报错了的插件,我几乎全都下载了一遍

- 到现在,之前所有的错误提示全部消失,不仅如此,我发现最新版本的vue居然是4.0+???

- WTF?

- 我之前用的可是2.6啊混蛋

- 难怪nanarino给我的项目那么简单,感情人家的已经是领先好几代了

  临近考试了,本来以为这次考试稳了,现在看来,要是不赶紧摸清楚新版本的变化,恐怕这次要跪啊!

  .

------

使用vue cli 4 的注意事项





- 创建语句      vue create projects_name
- 下载模块      npm install models_name   -g –save
- 构建vue工程之后第一点就是重新下载axios与pug相关依赖,具体可以根据报错提示进行操作

 