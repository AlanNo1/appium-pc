#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from utils.logger import logger
from common.readconfig import ini
from page_object.searchpage import SearchPage


@allure.feature("测试百度模块")
class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_chorem(self, drivers):
        """打开谷歌浏览器"""
        search = SearchPage(drivers)

    @allure.story("搜索selenium结果用例")
    def test_001(self, drivers):
        """搜索"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        result = re.search(r'selenium', search.get_source)
        logger.info(result)
        assert result


if __name__ == '__main__':
    pytest.main(['TestCase/test_search.py'])
# if __name__ == '__main__':
# 下面的代码使用pycharm运行可能会没有生成报告，建议使用vscode执行
#     import os
#     pytest.main(['TestCase/test_search.py', '--alluredir', './allure'])
#     os.system('allure serve allure')
