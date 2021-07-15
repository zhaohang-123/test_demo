# coding=utf-8
import unittest
from 自动化.测试框架.添加.CrmAddEmployee.Page.Base import base
import selenium.webdriver.common.by
import time


BY = selenium.webdriver.common.by
class Searchpage(base):
    # 找到左导航栏frame
    def search_frame_left(self):
        # return self.frame(self.driver.find_elements_by_tag_name('frame')[1])
        return self.driver.switch_to.frame(self.driver.find_elements_by_tag_name('frame')[1])
    # 找到中间窗口frame
    def search_frame_centre(self):
        # return self.frame('mainFrame')
        return self.driver.switch_to.frame('mainFrame')
    # 返回默认frame
    def search_frame_default(self):
        return self.driver.switch_to.default_content()
    # 找到添加员工
    def search_addEmployee(self):
        return self.find(BY.By.LINK_TEXT,'添加员工')
    # 性别
    def search_userSex(self):
        return self.find(BY.By.NAME,'userSex')
    # 学历userDiploma
    def search_userDiploma(self):
        return self.find(BY.By.NAME,'userDiploma')
    # 部门departmentId
    def search_departmentId(self):
        return self.find(BY.By.NAME,'departmentId')

    # 姓名输入框
    def search_userName(self):
        return self.find(BY.By.NAME, 'userName')
    # 年龄输入框
    def search_userAge(self):
        return self.find(BY.By.NAME, 'userAge')
    # 账号
    def search_userNum(self):
        return self.find(BY.By.NAME, 'userNum')
    # 密码
    def search_userPw(self):
        return self.find(BY.By.NAME, 'userPw')
    # 添加人
    def search_userAddman(self):
        return self.find(BY.By.NAME, 'userAddman')
    # 找到添加按钮
    def sreach_addbutton(self):
        return self.find(BY.By.NAME, 'submit')

    # def test_case(self,username,userage,usernum,userpw,useraddman):
    #     # 切换frame左
    #     time.sleep(2)
    #     self.search_frame_left()
    #     # 点击添加员工
    #     time.sleep(1)
    #     self.search_addEmployee().click()
    #     # 切换frame默认
    #     time.sleep(1)
    #     self.search_frame_default()
    #     # 切换frame中间
    #     self.search_frame_centre()
    #     time.sleep(1)
    #     # 输入姓名
    #     self.search_userName().send_keys(username)
    #     # 输入年龄
    #     self.search_userAge().send_keys(userage)
    #     # 输入账号
    #     self.search_userNum().send_keys(usernum)
    #     # 密码
    #     self.search_userPw().send_keys(userpw)
    #     # 添加人
    #     self.search_userAddman().send_keys(useraddman)