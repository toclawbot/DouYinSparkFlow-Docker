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

    # 移除所有手动修改 PLAYWRIGHT_BROWSERS_PATH 的逻辑
    # 让 Playwright 使用默认的系统路径 /ms-playwright
    
    if DEBUG:
        headless = False

    try:
        # 启动浏览器
        playwright = sync_playwright().start() 
        browser = playwright.chromium.launch(headless=headless)
        return playwright, browser
    except Exception as e:
        # 捕获浏览器启动错误
        traceback.print_exc()
