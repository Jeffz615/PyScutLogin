# encoding:utf-8

from PyScutLogin import PyScutLogin as psl
import requests as rq

session = psl('username', 'password',
              'http://jw2018.jw.scut.edu.cn/sso/driotlogin')  # 登录教务系统
# session.post(..., ...)  # POST操作
# session.get(..., ...)  # GET操作
