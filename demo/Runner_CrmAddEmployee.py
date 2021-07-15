# coding=utf-8
from 自动化.测试框架.添加.CrmAddEmployee.Case.testcase import TestCase
from 自动化.测试框架.添加.CrmAddEmployee.Page.Base import base
import unittest
from HTMLTestRunner import HTMLTestRunner
# HTMLTestRunner用来生成HTML格式的测试报告
import time
import os
# import 邮件发送2
from 自动化.测试框架.添加.CrmAddEmployee.Page import 邮件发送2


# import random
# xing = '王李张刘陈杨黄赵吴周徐孙马朱胡郭何高林罗郑梁谢宋唐位许韩冯邓曹彭曾萧田董潘袁于蒋蔡余杜叶程苏魏吕丁任沈姚卢姜崔钟谭陆汪范' \
#        '金石廖贾夏韦傅方白邹孟熊秦邱江尹薛阎段雷侯龙史陶黎贺顾毛郝龚邵万钱严覃武戴莫孔向汤'
# ming = '丹举义之乐书乾云亦从代以伟佑俊修健傲儿元光兰冬冰冷凌凝凡凯初力勤千卉半华南博又友同向君听和哲嘉国坚城夏夜天奇奥如妙子存季孤宇安宛宸寒寻' \
#        '尔尧山岚峻巧平幼康建开弘强彤彦彬彭心忆志念怀怜恨惜慕成擎敏文新旋旭昊明易昕映春昱晋晓晗晟景晴智曼朋朗杰松枫柏柔柳格桃梦楷槐正水沛波泽洁洋济浦浩海涛润涵渊源溥濮瀚灵灿炎烟烨然煊煜熙熠玉珊珍理琪琴瑜瑞瑶瑾璞痴皓盼真睿碧磊祥祺秉程立竹笑紫绍经绿群翠翰致航良芙芷苍苑若茂荣莲菡菱萱蓉蓝蕊蕾薇蝶觅访诚语谷豪赋超越轩辉达远邃醉金鑫锦问雁雅雨雪霖霜露青靖静风飞香驰骞高鸿鹏鹤黎'
# str1 = random(xing(2))
# print(str1)

username='itachi02'
userage='22'
usernum='itachi02'
userpw='123456'
useraddman='张三'
class CRM(unittest.TestCase):
    def run_crm(self):
        t_c=TestCase()
        t_c.test_case(username, userage, usernum, userpw, useraddman)
        print(username, userage, usernum, userpw, useraddman)


if __name__ == '__main__':
    time.sleep(2)
    # 测试套件，构建测试集
    suite = unittest.TestSuite()
    suite.addTest(CRM('run_crm'))
    # 我们要新建一个用于保存我们测试结果的文件，html
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    print(now)
    # 定义文件的名字
    filename = 'C:\\Users\\22405\\PycharmProjects\\untitled1\\自动化\\自动化测试模型'+now+"_result.html"
    print(filename)
    file = open(filename, "wb")
    # 执行我们的报告写入

    runner = HTMLTestRunner(stream=file, title="crm_员工添加测试报告", description="用例执行情况:")
    # stream：是指定测试报告文件
    # title：指定报告的标题
    # description:指定报告的副标题
    # 执行我们测试用例
    runner.run(suite)
    time.sleep(3)
    print(file.closed)
    # 要进行关闭
    file.close()
    print(file.closed)


    邮件发送2.send_mail(filename)