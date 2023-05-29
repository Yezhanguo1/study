import sys
import os

sys.path.append(os.path.dirname(sys.path[0]))
sys.path.append("C:\\Users\\Hasee\\PycharmProjects\\pythonProjectForWork")

# import allure
import pytest

from interfaceAutomationTest.API.loginapi import Login
from interfaceAutomationTest.Utils.util_log import getlog
from interfaceAutomationTest.common.user_excel import Excel

# from conftest import my_log

my_log = getlog()


# @allure.feature("登录模块")
class Test_show:
    @pytest.mark.parametrize('case_name,method, url, data, result',
                             Excel.read_case_excel(Excel(), file_path="C:/Users/Hasee/PycharmProjects/pythonProjectForWork/interfaceAutomationTest/case/test_case_date.xlsx", Sheel_name="denglu"))
    # @allure.story('登录场景')
    # @allure.title("用例名称：{case_name}")
    def test_01(self, case_name, method, url, data, result):
        resp = Login.test_dome(Login(), method=method, url=url, data=data)

        assert result == resp.status_code
        my_log.info(f"{case_name}||执行成功，实际结果-{resp.status_code}-符合预期")


if __name__ == '__main__':
    pytest.main(["test_casedome.py", "-s", "--alluredir", "../reports/date"])
    os.system("allure generate ../reports/date -o ../reports/html_report --clean")
