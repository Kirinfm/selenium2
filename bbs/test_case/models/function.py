import os

from bbs.test_case.models.driver import browser


def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]
    file_path = base + "/report/image/" + file_name
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = browser()
    driver.get("https://icmp2.propersoft.cn/icmp/propersoft/#/base/login")
    insert_img(driver, 'login.png')
    driver.quit()
