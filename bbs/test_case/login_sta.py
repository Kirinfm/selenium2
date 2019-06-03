import unittest
from time import sleep

from bbs.test_case.models import myunit, function
from bbs.test_case.page_obj.loginPage import login


class loginTest(myunit.MyTest):
    def test_login(self):
        login(self.driver).user_login("admin", "123456")
        sleep(3)
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), "超级管理员")
        function.insert_img(self.driver, "user_success.jpg")

    def test_login_fail(self):
        login(self.driver).user_login("admin", "")
        sleep(3)
        po = login(self.driver)
        function.insert_img(self.driver, "user_fail.jpg")


if __name__ == "__main__":
    unittest.main()
