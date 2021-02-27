
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWework():
    """定义企业微信类"""
    def setup(self):
        """setup方法"""
        self.driver = webdriver.Chrome()
        # 隐式等待5s
        self.driver.implicitly_wait(5)

    def teardown(self):
        """teardown方法"""
        self.driver.quit()

    def test_cookie(self):
        """获取cookies方法"""
        # 获取cookies
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # 创建一个保存cookie的文件
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850783936872'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850783936872'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614391300'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645927300, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614178301,1614178306,1614179127,1614391231'}, {'domain': '.qq.com', 'expiry': 1903174142, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_1083260284'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'cCTSk7xJJHfl3YECnZXY8rOoiYIQx7ASGA7RCW0sYeChSMInDjHbH2AdoI4PcBMtXy9jR-BKtI3jyPf0GgISWA9B-0YgA0mKPb_iq3e-wZd1q2ip3tWUpXgYW5sjwXn-62ALxy9OfQHhYSrLbNIYSSi_8mcSwdDxi-PMJJEQIAjexJpH1pjMjOHn8Ef8EWNP4Ymu083V8yMX8l5NZeXgtwkKVNVvkrCTdB5XRTGh7PsYLC9NHE1NeWNx307N9WDobMT4CupirttXXJoxqgJqcA'}, {'domain': '.qq.com', 'expiry': 1619350130, 'httpOnly': True, 'name': 'ied_qq', 'path': '/', 'secure': False, 'value': 'o1083260284'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '8219889746829'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'RyHQO-vMqPuNjfd20v3lJdPj1W2ZktezF8FGREO4nCIY7r2Srn3noxtGyfVpKud1'}, {'domain': '.qq.com', 'expiry': 1614477822, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1642521855.1614391231'}, {'domain': 'work.weixin.qq.com', 'expiry': 1614422766, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': 'onkar7'}, {'domain': '.qq.com', 'expiry': 1891651874, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '3b9386062b8db584'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645714023, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1677463422, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1822611966.1586156816'}, {'domain': '.work.weixin.qq.com', 'expiry': 1616983425, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1645063122, 'httpOnly': False, 'name': 'eas_sid', 'path': '/', 'secure': False, 'value': 'C1Y6m1P3k5w2m7a1d2w2c394g1'}, {'domain': '.qq.com', 'expiry': 1634712054, 'httpOnly': False, 'name': 'LOLWebSet_AreaBindInfo_1083260284', 'path': '/', 'secure': False, 'value': '%257B%2522areaid%2522%253A%252215%2522%252C%2522areaname%2522%253A%2522%25E6%259A%2597%25E5%25BD%25B1%25E5%25B2%259B%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221083260284%2522%252C%2522rolename%2522%253A%2522%25E8%258F%259C%25E9%25B8%25A1%25E6%259C%25A8%25E5%258D%2597%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1083260284%257C15%257C1083260284*%257C%257C%257C%257C%2525E8%25258F%25259C%2525E9%2525B8%2525A1%2525E6%25259C%2525A8%2525E5%25258D%252597*%257C%257C%257C1603175992%257C%2522%252C%2522md5str%2522%253A%2522ABCB5D349EA00099BC4E1FFE6A267D8F%2522%252C%2522roleareaid%2522%253A%252215%2522%252C%2522sPartition%2522%253A%252215%2522%257D'}, {'domain': '.qq.com', 'expiry': 1634712060, 'httpOnly': False, 'name': 'uin_cookie', 'path': '/', 'secure': False, 'value': 'o1083260284'}, {'domain': '.qq.com', 'expiry': 1903174158, 'httpOnly': False, 'name': 'mobileUV', 'path': '/', 'secure': False, 'value': '1_171b1194f15_681ab'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '797e7b2ccc5feec4c99f0bdd9f0f9694c819ac77ac945038634e0a6883cb86ee'}, {'domain': '.qq.com', 'expiry': 2147483692, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': '25DkEcmJOb'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325116429447'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '2106492928'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '5413939680'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7997466'}, {'domain': '.qq.com', 'expiry': 7882233194, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%2216eb74ad8457a3-0949d50df4d028-2393f61-3686400-16eb74ad846b83%22%2C%22%24device_id%22%3A%2216eb74ad8457a3-0949d50df4d028-2393f61-3686400-16eb74ad846b83%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D'}, {'domain': '.qq.com', 'expiry': 1634712083, 'httpOnly': False, 'name': 'LW_sid', 'path': '/', 'secure': False, 'value': 'b1R6R0a361R766b088Q3q4w0A2'}]
        # db = shelve.open('./mydbs/cookies')
        # db['cookie'] = cookies
        # db.close()
        pass


    def test_wework(self):
        """使用cookie登录企业微信，完成导入联系人，加上断言验证"""
        # 打开数据库文件
        db = shelve.open('./mydbs/cookies')
        # 获取存储的cookies
        cookies = db['cookie']
        # 打开企业微信页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 使用cookies进行登录
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # sleep(3)
        # 点击导入联系人
        self.driver.find_element_by_css_selector('.index_service_cnt_itemWrap:nth-child(2)').click()
        # 将文件进行上传
        self.driver.find_element_by_id('js_upload_file_input').send_keys('C:\\Users\\邓晶明\\Desktop\\mydata.xlsx')
        # 断言text属性相等
        assert 'mydata.xlsx' == self.driver.find_element_by_id('upload_file_name').text

    def test_add_member(self):
        """添加成员方法"""
        db = shelve.open('./mydbs/cookies')
        cookies = db['cookie']
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element_by_css_selector('.index_service_cnt_itemWrap:nth-child(1)').click()
        self.driver.find_element_by_id('username').send_keys('d')
        self.driver.find_element_by_id('memberAdd_english_name').send_keys('poppy')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('1')
        self.driver.find_element_by_id('memberAdd_phone').send_keys('13112341234')
        self.driver.find_element_by_link_text('保存').click()
        assert '13112341234' == self.driver.find_element_by_xpath('//*[@id="member_list"]/tr[1]/td[5]').text





