#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/28 23:41
# @Author  : zhaoyang
# @File    : test_calc.py

import pytest
import allure
import yaml
import decimal
from pytest_live_1.core.calc import Calc

# 测试数据准备
data = yaml.safe_load(open("../data.yaml"))

# 限制计算精度,小数点后8位
decimal.getcontext().prec = 8

class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a, b", data)
    def test_mul(self, a, b):
        with allure.step("数据检测"):
            # 参数为int或float或能转化为int,float类型
            if (isinstance(a, (int, float)) and isinstance(b, (int, float))) \
                    or (int(a) and int(b)) \
                    or (int(a) and float(b)) \
                    or (float(a) and int(b)) \
                    or (float(a) and float(b)):
                r1 = decimal.Decimal(self.calc.mul(a, b) * decimal.Decimal(1))
                r2 = decimal.Decimal(a) * decimal.Decimal(b)
                with allure.step("结果校验"):
                    assert r1 == r2
            else:
                with pytest.raises(TypeError, ValueError):
                    pass

    @pytest.mark.parametrize("a, b", data)
    def test_div(self, a, b):
        with allure.step("数据检测"):
            if (isinstance(a, (int, float)) and isinstance(b, (int, float))) \
                    or (int(a) and int(b)) \
                    or (int(a) and float(b)) \
                    or (float(a) and int(b)) \
                    or (float(a) and float(b)):
                with allure.step("除数为0"):
                    if b == 0:
                        with pytest.raises(ZeroDivisionError):
                            pass
                    else:
                        r1 = decimal.Decimal(self.calc.mul(a, b) / decimal.Decimal(1))
                        r2 = decimal.Decimal(a) / decimal.Decimal(b)
                        with allure.step("结果校验"):
                            assert r1 == r2
            else:
                with pytest.raises(TypeError, ValueError):
                    pass

if __name__ == '__main__':
    pytest.main()