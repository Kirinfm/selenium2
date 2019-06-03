from selenium.webdriver import Remote


def browser():
    host = '192.168.13.1:16679'
    dc = {'browserName': 'chrome',
          'version': '74.0.3729.131',
          'platform': 'ANY'}
    driver = Remote(command_executor='http://' + host + '/wd/hub',
                    desired_capabilities=dc)
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("https://icmp2.propersoft.cn/icmp/propersoft/#/base/login")
    dr.quit()
