import pytest
import allure
import logging


@allure.step("测试步骤1：xxx")
def step_1(env):
    logging.info("测试步骤1：xxx ...")
    # 编写步骤1的内容，比如这里打印env.ip
    logging.info(env.ip)

@allure.step("测试步骤2：xxx")
def step_2(env):
    logging.info("测试步骤2：xxx ...")
    # 编写步骤1的内容，比如这里打印env.username 和 env.password
    logging.info(env.username)
    logging.info(env.password)


@allure.feature("功能：xxx")
@allure.issue(url="www.xxx.com",name="需求来源于xxx")
@allure.link(url="www.xxx.com",name="需求文档地址")
@allure.story("用户故事：xxx")
@allure.severity('normal')
@allure.title("测试用例：xxxc")
@allure.description("测试用例描述：xxx")
def test_api_01(env):
    step_1(env)
    step_2(env)