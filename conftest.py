#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import base64
import pytest
import allure
from py.xml import html
from appium.webdriver import Remote
from config.conf import settings
from common.readconfig import ini
from utils.times import timestamp
from utils.send_mail import send_report

driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        desired_capabilities = {
            "app": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "platform_name":"Windows"}
        driver = Remote(
            command_executor='http://127.0.0.1:4747',
            desired_capabilities=desired_capabilities)
        # driver.maximize_window()

    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver