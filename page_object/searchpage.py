#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

search = Element('search')


class SearchPage(WebPage):
    """搜索类"""

    def input_search(self, content):
        """输入搜索"""
        self.input_text(search['搜索框'], txt=content)
        sleep()

    def click_search(self):
        """点击搜索"""
        self.click(search['搜索按钮'])


if __name__ == '__main__':
    pass
