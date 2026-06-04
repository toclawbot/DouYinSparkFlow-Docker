# Docker 部署指南

本项目已由 Aida 封装为 Docker 镜像，旨在提供一个开箱即用的运行环境，无需手动配置 Python 或浏览器依赖。

## 快速开始

### 1. 准备配置文件
在项目根目录下创建 `.env` 文件。您可以利用项目提供的 [配置生成器](https://github.com/litemini/DouYinSparkFlow/blob/main/docs/%E9%85%8D%E7%BD%AE%E7%94%9F%E6%88%90%E5%99%A8%E4%BD%BF%E7%94%A8.md) 生成配置内容并粘贴进去。

### 2. 启动容器
使用 Docker Compose 一键启动：

```bash
docker-compose up -d
```

### 3. 查看日志
检查脚本运行状态：

```bash
docker logs -f douyin-spark-flow
```

## 维护操作

- **更新配置**：修改 `.env` 文件后，重启容器即可生效：
  ```bash
  docker-compose restart
  ```

- **更新代码**：如果项目源码有更新，重新构建镜像：
  ```bash
  docker-compose up -d --build
  ```

- **停止运行**：
  ```bash
  docker-compose down
  ```

## 封装技术细节
- **基础镜像**: `mcr.microsoft.com/playwright/python:jammy` (由微软官方提供，包含完整浏览器环境)。
- **运行模式**: 完全 Headless (无头模式)，适配服务器部署。
- **持久化**: 通过挂载 `.env` 文件实现配置与镜像的分离。

😊
