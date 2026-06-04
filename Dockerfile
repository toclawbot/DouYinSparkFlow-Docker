# 使用官方 Playwright Python 镜像，内置所有浏览器依赖
FROM mcr.microsoft.com/playwright/python:jammy

# 设置工作目录
WORKDIR /app

# 避免 Python 产生 .pyc 文件
ENV PYTHONDONTWRITEBYTECODE=1
# 强制 stdout/stderr 实时输出，不进入缓存
ENV PYTHONUNBUFFERED=1

# 1. 安装基础依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. 拷贝项目源代码
COPY . .

# 3. 预安装浏览器二进制文件 (确保版本一致)
# 虽然基础镜像自带，但为了防止 requirements.txt 更新了 playwright 版本导致不匹配，执行一次安装
RUN playwright install chromium

# 运行脚本
CMD ["python", "main.py"]
