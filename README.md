# PyScutLogin

这是个python的包（虽然里面只有一个函数），用来登录华南理工大学的统一认证平台。

## 环境

**python 3** + **PyExecJS**

## 证书

**GPL**

## 为什么要开源？

写个轮子大家一起用

## 它有什么用？

可以通过统一认证登录各种服务，然后编写属于你的脚本（这就需要你发挥想象力了）。

## 它怎么用？

首先你需要装PyExecJS包。`linux中使用PyExecJS包还需要JS环境，如nodejs`

```shell
pip install PyExecJS
```

然后把PyScutLogin文件夹放进你项目的目录里。

最后你就可以在你的代码里**import PyScutLogin**了

------

调用包里面的函数会返回一个**requests.session**类，至于这个类怎么用，你可以上网谷歌/百度。

`example.py`

```python
# encoding:utf-8

from PyScutLogin import PyScutLogin as psl
import requests as rq

session = psl('username', 'password',
              'http://jw2018.jw.scut.edu.cn/sso/driotlogin')  # 登录教务系统
# session.post(..., ...)  # POST操作
# session.get(..., ...)  # GET操作
```

