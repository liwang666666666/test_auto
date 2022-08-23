import pytest

def pytest_addoption(parser):
    parser.addoption("--flash", action="store", default="China",help="set flash")
    parser.addoption("--update", action="store", default="China", help="set update")

@pytest.fixture(scope="class",)
def flash(request):
    return request.config.getoption("--flash")

@pytest.fixture(scope="class",)
def update(request):
    return request.config.getoption("--update")










# # content of conftest.py
# import pytest
#
# # 注册自定义参数 enr 到配置对象
# def pytest_addoption(parser):
#     """
#     pytest_addoption 可以让用户注册一个自定义的命令行参数，方便用户将数据传递给 pytest；
#     这个 Hook 方法一般和 内置 fixture pytestconfig 配合使用，pytest_addoption 注册命令行参数，
#     pytestconfig 通过配置对象读取参数的值；
#     :param parser:
#     :return:
#     """
#     parser.addoption("--enr", action="store", default="test", help="full")
#
# # 从配置对象获取enr的值，
# @pytest.fixture(scope='session', autouse=True)
# def enr(pytestconfig, glb=None):
#     """
#     获取运行环境并设置全局变量
#     :param pytestconfig:
#     :return:
#     """
#     glb.enr = pytestconfig.getoption("--enr")

# import pytest
# from configparser import ConfigParser
# def pytest_addoption(parser):
#     """
#     增加参数 env
#     """
#     parser.addoption("--env", action="store", default="deeptables",
#                      help="one of: deeptables, gbm")
#
# @pytest.fixture(scope="session")
# def get_host(pytestconfig):
#     """
#     调用该函数返回对应的host
#     """
#     env = pytestconfig.getoption('--env')
#     return env