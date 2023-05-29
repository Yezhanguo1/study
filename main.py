# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


# 按间距中的绿色按钮以运行脚本。
import os

import pytest

if __name__ == '__main__':
    pytest.main(
        ["-s","C:/Users/Hasee/PycharmProjects/pythonProjectForWork/interfaceAutomationTest/case/test_casedome.py"])
    os.system("allure generate C:/Users/Hasee/PycharmProjects/pythonProjectForWork/interfaceAutomationTest"
              "/reports/date -o C:/Users/Hasee/PycharmProjects/pythonProjectForWork/interfaceAutomationTest"
              "/reports/html_report --clean")
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
# "C:/Users/Hasee/PycharmProjects/pythonProjectForWork/interfaceAutomationTest/case/test_casedome.py",
