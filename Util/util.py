import subprocess
import sys

'''
工具类
'''


def func_adb_with_result(cmd):
    # 执行adb命令，返回字符串
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    out = str(output, encoding='utf-8')
    return out


def terminal_exec(shell):
    # 执行cmd命令，如果成功，返回0, 如果失败，返回1
    res = subprocess.Popen(shell, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)  # 使用管道
    res.communicate()
    return res.returncode


def terminal_exec_with_list(cmd):
    # 执行cmd命令，返回list
    result = []
    res = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # 使用管道
    out = res.stdout.readlines()  # 获取输出结果
    for line in out:
        result.append(line)
    res.wait()  # 等待命令执行完成
    res.stdout.close()  # 关闭标准输出
    return result
