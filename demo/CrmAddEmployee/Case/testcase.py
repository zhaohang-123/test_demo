# coding=utf-8
from 自动化.测试框架.添加.CrmAddEmployee.PageObject.AddEmployee import Searchpage
import time
class TestCase(Searchpage):
    def test_case(self, username, userage, usernum, userpw, useraddman):
        # 切换frame默认
        time.sleep(1)
        self.search_frame_default()
        # 切换frame左
        time.sleep(2)
        self.search_frame_left()
        '''-----------------'''
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[4]/td/'
                                          'table/tbody/tr[1]/td/table/tbody/tr/td[2]').click()
        '''-----------------'''
        # 点击添加员工
        time.sleep(1)
        self.search_addEmployee().click()
        # 切换frame默认
        time.sleep(1)
        self.search_frame_default()
        # 切换frame中间
        self.search_frame_centre()
        time.sleep(1)
        # 输入姓名
        self.search_userName().send_keys(username)
        # 输入年龄
        self.search_userAge().send_keys(userage)
        # 输入账号
        self.search_userNum().send_keys(usernum)
        # 密码
        self.search_userPw().send_keys(userpw)
        # 添加人
        self.search_userAddman().send_keys(useraddman)
        # 点击添加按钮
        time.sleep(1)
        self.sreach_addbutton().click()
