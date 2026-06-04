import os, sys
import subprocess
import traceback
from playwright.sync_api import sync_playwright
from utils.config import DEBUG, get_environment, Environment

PLAYWRIGHT_BROWSERS_PATH = "../chrome"

def install_browser():
    """
    安装 Chromium 浏览器
    """
    try:
        subprocess.run(["playwright", "install", "chromium"], check=True)
        print("浏览器安装完成，请重新运行程序。")
    except subprocess.CalledProcessError as e:
        print(f"发生未知错误：{e}")


def get_browser():
    """
    启动浏览器实例
    :return: 浏览器实例
    """

    headless = True

    try:
        # 启动浏览器
        playwright = sync_playwright().start() 
        # 增加关键参数，彻底解决 Linux/Docker 平台初始化失败问题
        browser = playwright.chromium.launch(
            headless=headless,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu"
            ]
        )
        return playwright, browser
    except Exception as e:
        traceback.print_exc()
        print("❌ 浏览器启动失败，请检查环境变量或镜像完整性。")
        sys.exit(1) # 失败时直接退出进程，而不是返回 None 导致后续解包崩溃
