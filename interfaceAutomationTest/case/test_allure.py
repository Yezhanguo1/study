import pytest
import allure

class Test_Allure:
    def test_1(self):
        a=1
        b=a+1
        assert b==2
    def test_2(self):
        c="a"
        d="cfaf"
        assert c in d
    def test_3(self):
        assert 1!= 3
    def test_4(self):
        assert "ddd" == "ccc"


if __name__ == '__main__':
    pytest.main(["test_allure.py","-s","--alluredir","../reports/date"])

