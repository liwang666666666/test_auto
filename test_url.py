import os
import zipfile
import allure
import pytest
import shutil
import time
from Util.util import *


@pytest.fixture(scope='class', autouse=True)
def getini(pytestconfig):
    print(pytestconfig.getini('addopts'))
    print(pytestconfig.getini('log_cli'))

build = './liwang'
end='./ota'

@pytest.fixture(scope='class', autouse=True)
def test_demo(flash,update):
    print(flash,update)
    if (os.path.exists(build)):
        shutil.rmtree(build)
    print('旧镜像删除成功')
    os.system('wget -P ./liwang --http-user=software --http-password=software123 --auth-no-challenge ' + flash)
    if (os.path.exists(end)):
        shutil.rmtree(end)
    print('旧升级包删除成功')
    os.system('wget -P ./ota --http-user=software --http-password=software123 --auth-no-challenge ' + update)
    path = './ota'
    datanames = os.listdir(path)
    for i in datanames:
        n = i.split('.')
    new_i ="update"  # 在此处有区别：把想要增加的内容，以字符串的形式放在末尾即可
    new_name = new_i + '.zip'
    if i.endswith(".zip"):  # 判断是否是.zip文件
        os.rename(os.path.join(path, i), os.path.join(path, new_name))
    print('升级包改名成功')
    
    otapackage = './ota/update.zip'
    sz = os.path.getsize(otapackage)
    print(sz)
    if sz > 100000000:
        print('此次为全量包ota测试')
    else:
        print('此次为差量包ota测试')

    path = './liwang/'
    L = []
    for root, dirs, files in os.walk(path):
        for file in files:
            L.append(file)
        for i in L:
            zip = zipfile.ZipFile(path + i, 'r')
            zip.extractall(path='./liwang/')
            zip.close()
    print('解压镜像包ok')
    #解压liwang文件夹下的所有zip文件

    time.sleep(10)
    os.chdir('./liwang/fastboot_build')
    #切换到fastboot-all.sh目录
    currentPath = os.getcwd().replace('\\','/')    # 获取当前路径
    print(currentPath)
    os.system('chmod 777 fastboot-all.sh')
    # #sh脚本加权限
    os.system('./fastboot-all.sh')
    # 烧录版本到飞机
    time.sleep(10)
    os.chdir('../..')
    currentPath = os.getcwd().replace('\\', '/')  # 获取当前路径
    print(currentPath)
    #切换路径到根目录，否则第2次执行会出问题
    time.sleep(10)
    version = func_adb_with_result('adb shell "./cheerios/tests/cli dis_ver"')
    print(version)
    time.sleep(10)

@allure.step('recovery测试')
def test_ota_update_status():
    os.system('adb wait-for-device')
    os.system('adb push ./ota/update.zip /data')
    os.system('bash ./shell/bleliwang6.sh')
    time.sleep(5)
    os.system('python3 ble.py --ota_update_request request_type 2')
    # os.system('tail -f /tmp/recovery.log')
    time.sleep(120)
    ota_update_status = func_adb_with_result('adb shell "cat /cache/recovery/ota_update_status"')
    # print(ota_update_status)
    print('adb shell "cat /cache/recovery/ota_update_status"')
    if ota_update_status != 'FAILED':
        print('upgrade success!')
        os.system('adb shell "cat /tmp/recovery.log"')
        print('adb shell "cat /tmp/recovery.log"')
        time.sleep(10)
        os.system('python3 ble.py --ota_update_request request_type 6')
        os.system('adb wait-for-device')
        time.sleep(30)
        version=func_adb_with_result('adb shell "./cheerios/tests/cli dis_ver"')
        print('升级成功'+ version)
        assert True
    else:
        result = func_adb_with_result('adb shell "cat /cache/recovery/ota_update_status"')
        print('升级失败'+ result)
        os.system('adb pull data/log/latest 失败log')
        version = func_adb_with_result('adb shell "./cheerios/tests/cli dis_ver"')
        print(version)
        assert False
