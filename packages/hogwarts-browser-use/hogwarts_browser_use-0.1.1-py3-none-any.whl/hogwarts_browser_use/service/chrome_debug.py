"""
  @Author: 天马
  @Date: 2025/2/7
  @Desc: 
"""
import os
import subprocess
import sys


def kill_chrome():
    try:
        if sys.platform == 'win32':
            # Windows系统使用taskkill命令
            subprocess.run(
                ['taskkill', '/IM', 'chrome.exe', '/F'],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )
        elif sys.platform in ('linux', 'darwin'):
            # Linux/Mac系统使用pkill命令
            process_name = 'chrome' if sys.platform == 'linux' else 'Google Chrome'
            subprocess.run(
                ['pkill', '-f', process_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )
    except subprocess.CalledProcessError:
        # 忽略找不到进程的错误
        pass


def start_chrome_debug():
    port = 9222  # 调试端口
    chrome_command = []

    if sys.platform == 'win32':
        # Windows系统命令
        chrome_path = os.path.join(
            os.environ.get('ProgramFiles', 'C:\\Program Files'),
            'Google\\Chrome\\Application\\chrome.exe'
        )
        chrome_command = [chrome_path, f'--remote-debugging-port={port}']
    elif sys.platform == 'linux':
        # Linux系统命令
        chrome_command = ['google-chrome', f'--remote-debugging-port={port}']
    elif sys.platform == 'darwin':
        # MacOS系统命令
        chrome_command = [
            '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
            f'--remote-debugging-port={port}'
        ]

    try:
        subprocess.run(chrome_command, check=True)
    except FileNotFoundError:
        # 如果默认路径无效，尝试PATH环境变量中的命令
        if sys.platform == 'win32':
            subprocess.run(f'start chrome --remote-debugging-port={port}', shell=True)
        elif sys.platform == 'darwin':
            subprocess.run(['open', '-a', 'Google Chrome', '--args', f'--remote-debugging-port={port}'])


def start():
    try:
        res = input("即将关闭全部Chrome浏览器，输入Y继续...")
        if res.lower() != 'y':
            print("❌ 操作已取消")
            sys.exit(1)
        kill_chrome()
        start_chrome_debug()
        print("✅ Chrome已以调试模式重新启动")
    except Exception as e:
        print(f"❌ 操作失败: {str(e)}")
        sys.exit(1)
