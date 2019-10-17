"""
    项目架构:
    核心: api + case +data
    api: 封装请求相关业务(使用requests向服务器发送请求)
    case:封装unittest (调用api的请求业务,参数化调用data中的数据,还需要实现断言业务)
    data:封装测试数据
    
    测试报告: report + tools +run_suite
    report:保存生成测试报告
    tools:存放第三方工具
    run_suite:组织测试套件
    
    全局文件:app.py
    封装程序中的常量/全局变量/工具方法
    
"""

# 封装不同接口中的URL相同的前缀(协议+域名)
import os

login_URL = "http://localhost/"

URl = os.getcwd()