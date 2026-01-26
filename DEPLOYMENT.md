# 阿里云 Docker 部署指南 (Alibaba Cloud Docker Deployment Guide)

本指南将指导您将 Tech Blog 项目部署到阿里云 ECS 服务器。我们使用 Docker 和 Docker Compose 来简化部署流程。

## 1. 准备工作

### 1.1 获取服务器信息
在阿里云控制台获取以下信息：
*   **公网 IP (Public IP)**: 例如 `123.45.67.89`
*   **SSH 登录密码**: 如果是密钥对，请确保私钥在本地。

### 1.2 域名准备 (可选)
如果您拥有域名 (例如 `example.com`)：
1.  登录域名提供商控制台。
2.  添加 **A 记录**，主机记录 `@`，记录值填写服务器的 **公网 IP**。

### 1.3 阿里云安全组设置
**非常重要**：确保阿里云 ECS 实例的 **安全组 (Security Group)** 入方向规则开放了以下端口：
*   **22** (SSH)
*   **80** (HTTP)
*   **443** (HTTPS) - 如果需要配置 SSL
*   **8000** (后端 API，可选，仅调试用，生产环境建议关闭)

---

## 2. 连接服务器与环境配置

### 2.1 SSH 连接服务器
在本地终端 (PowerShell 或 CMD) 执行：
```bash
ssh root@<您的公网IP>
# 输入密码登录
```

### 2.2 安装 Docker & Docker Compose
我们提供一个快速安装脚本 (适用于 Ubuntu/Debian/CentOS)。在服务器上执行：

```bash
# 安装 Docker
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun

# 启动 Docker 并设置开机自启
systemctl start docker
systemctl enable docker

# 安装 Docker Compose (V2)
# Docker 较新版本已内置 compose，通过 docker compose version 检查
# 如果没有，请安装插件:
apt-get update && apt-get install -y docker-compose-plugin
# 或者 CentOS: yum install -y docker-compose-plugin
```

sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://mirror.aliyuncs.com", "https://dockerproxy.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

**⚠️ 注意：**
最近国内 Docker Hub 访问受限，如果遇到 `i/o timeout` 错误，请务必执行上述配置。
阿里云 ECS 用户也可以在阿里云容器镜像服务控制台获取专属加速器地址。

验证安装：
```bash
docker --version
docker compose version
```

---

## 3. 部署代码

### 3.1 上传代码
您可以选择 **Git Clone** (推荐) 或 **SCP 上传**。

**方法 A: Git Clone (推荐)**
如果您的代码在 GitHub/Gitee：
```bash
# 在服务器上
mkdir -p /data/www
cd /data/www
git clone <您的仓库地址> tech_blog
cd tech_blog
```

**方法 B: SCP 上传**
如果不方便使用 Git，可以在**本地电脑**使用 SCP 命令上传：
```bash
# 在本地项目根目录执行
scp -r . root@<您的公网IP>:/data/www/tech_blog
```

### 3.2 配置环境变量
在服务器项目目录 (`/data/www/tech_blog`) 下：

1.  **后端 .env**:
    ```bash
    cp backend/.env backend/.env.prod
    vim backend/.env.prod
    ```
    修改以下内容以适配生产环境：
    ```ini
    DEBUG=False
    SECRET_KEY=请修改为一个复杂的随机字符串
    ALLOWED_HOSTS=<您的公网IP>,<您的域名>,localhost,127.0.0.1,backend
    MYSQL_PASSWORD=<设置一个强密码>
    MYSQL_ROOT_PASSWORD=<设置一个强密码>
    MYSQL_HOST=db
    # 下面两项用于生产环境安全 (格式: http://您的域名,https://您的域名)
    CORS_ALLOWED_ORIGINS=http://<您的公网IP>,http://<您的域名>
    CSRF_TRUSTED_ORIGINS=http://<您的公网IP>,http://<您的域名>
    ```
    *(注意：本项目建议您将所有环境变量统一配置在根目录的 `.env` 文件中供 Docker Compose 读取。如果使用 `deploy.sh`，建议检查根目录 `.env` 是否包含上述所有配置)*

2.  **前端 .env**:
    前端构建需要知道 API 地址。
    ```bash
    vim frontend/.env.production
    ```
    确保内容为：
    ```
    VITE_API_URL=/api
    ```
    *(因为 Nginx 会处理 /api 转发，所以这里用相对路径即可)*

---

## 4. 构建与启动

### 4.1 一键部署 (推荐)
我们为您准备了一个自动化脚本 `deploy.sh`，它会自动构建前端并使用生产环境配置启动服务。

1.  **赋予脚本执行权限**：
    ```bash
    chmod +x deploy.sh
    ```
2.  **执行部署**：
    ```bash
    ./deploy.sh
    ```

3.  **配置 Nginx 域名 (可选)**
    如果需要绑定域名，修改 `nginx/nginx.conf`：
    ```bash
    vim nginx/nginx.conf
    ```
    找到 `server_name localhost;` 修改为 `server_name <您的域名> <公网IP>;`
    然后重启 Nginx 容器：
    ```bash
    docker compose restart nginx
    ```

### 4.2 手动分步执行 (如果不使用脚本)
如果您想了解细节，也可以手动执行以下命令：

**1. 构建前端**:
```bash
docker run --rm \
    -v $(pwd)/frontend:/app \
    -w /app \
    node:lts \
    /bin/sh -c "npm install && npm run build"
```

**2. 启动服务**:
使用 `docker-compose.prod.yml` (该配置更安全，不会暴露数据库端口到公网)：
```bash
docker compose -f docker-compose.prod.yml up -d --build
```

### 4.3 初始化数据库 (首次部署只需要运行一次)
```bash
# 1. 执行数据库迁移
docker compose -f docker-compose.prod.yml exec backend python manage.py migrate

# 2. 收集静态文件 (后台管理样式)
docker compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --noinput

# 3. 创建超级管理员
docker compose -f docker-compose.prod.yml exec backend python manage.py createsuperuser
```

---

## 5. 验证与维护

### 5.1 验证
在浏览器访问 `http://<您的公网IP>` 或 `http://<您的域名>`。
*   主页应正常显示。
*   尝试登录后台 `/admin`。

### 5.2 常用维护命令
*   **查看日志**: `docker compose logs -f`
*   **重启服务**: `docker compose restart`
*   **停止服务**: `docker compose down`
*   **更新代码**:
    ```bash
    git pull
    # 重新执行部署脚本 (会自动重新构建前端)
    ./deploy.sh
    ```

---

## 6. (进阶) 配置 HTTPS

如果是生产环境，建议配置 SSL。您可以修改 `nginx/nginx.conf` 挂载证书，或者使用 `certbot`。
最简单的方法是在宿主机安装 Nginx 作为反向代理，并使用 Certbot，将流量转发给 Docker 的 80 端口，或者在 Docker 内部配置 Certbot。
为保持简单，本指南暂仅包含 HTTP 部署。
