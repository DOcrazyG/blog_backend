# FastAPI + SQLalchemy + MySQL实现博客后端 API

参考（其实是copy!）([FastAPI 实战项目教程：构建完整的博客 API - IT-手册](https://buffaloboyhlh.github.io/it-handbooks/Web篇/FastAPI/practice/#6))上的项目描述实现的博客后端案例，可以用于fastAPI练手。

## 环境配置

```bash
python3 -m venv venv
source venv/bin/activate  # Linux激活虚拟环境
.\venv\Scripts\activate  # Windows激活虚拟环境

pip install -r requirements.txt
```


## 项目架构

```properties
blog_api_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── articles.py
│   │   └── comments.py
│   ├── schemas.py
│   └── auth.py
```

- `app/`：主要应用代码，包括数据库、模型、API 路由等。
- `main.py`：代码执行入口。
- `database.py`：mysql数据库连接配置。
- `models.py`：mysql数据库表结构的设计。
- `routers/`：不同功能模块的 API 路由。
- `schemas.py`：pydantic定义请求和响应数据结构。
- `auth.py`：JWT 认证逻辑。