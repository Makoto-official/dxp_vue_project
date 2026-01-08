# dxp_vue_project
数据库实训项目

## 快速运行（Windows）

下面给出在 Windows 环境下快速启动后端（Django）和前端（Vite）的步骤。假设仓库根目录为项目根。

### 前置要求
- 安装 Python 3.8+（用于后端）
- 安装 Node.js（含 npm 或 yarn，用于前端）
- 可选：Git

---

### 启动后端（Django）
后端工程位于 `dxp_movies_admin` 目录。

1. 进入后端目录并创建虚拟环境：

```powershell
cd dxp_movies_admin
python -m venv venv
venv\Scripts\Activate.ps1   # PowerShell
# 或者使用 cmd:
# venv\Scripts\activate.bat
```

2. 安装依赖：

```powershell
# 如果仓库中有 requirements.txt：
if (Test-Path requirements.txt) { pip install -r requirements.txt } else { pip install django }
```

3. 应用数据库迁移并运行服务：

```powershell
python manage.py migrate
python manage.py createsuperuser   # 如需创建管理员账户（可选）
python manage.py runserver 0.0.0.0:8000
```

后端默认会在 http://localhost:8000 提供服务。

---

#### 使用模拟数据
项目内置了模拟数据支持，方便在未连接真实数据库时进行开发与调试：

- 开关位置：在 `dxp_movies_admin/dxp_movies_admin/settings.py` 中，`USE_REAL_DATABASE` 配置用于控制数据源：
	- `False`：使用代码内置的模拟数据（默认）。
	- `True`：使用真实数据库（需要正确配置 `DATABASES` 并运行迁移）。
- 模拟数据文件：`dxp_movies_admin/movieslib/mock_data.py`，可直接编辑其中的数据列表以添加或修改示例数据。
- 特性：模拟数据为内存模式，服务重启后所有更改会丢失；写操作在模拟模式下只影响运行时内存，不会写入 `db.sqlite3`。

如果需要切换到真实数据库，请把 `USE_REAL_DATABASE` 设为 `True`，配置 `DATABASES` 并运行：

```powershell
python manage.py migrate
```


### 启动前端（Vite）
前端工程位于 `dxp_vite_project` 目录。

1. 进入前端目录并安装依赖：

```powershell
cd ..\dxp_vite_project
npm install
# 或者使用 yarn:
# yarn
```

2. 启动开发服务器：

```powershell
npm run dev
```

Vite 默认会在类似 http://localhost:5173 的地址启动开发服务器，终端会显示确切 URL。

---

### 开发时后端/前端联调（提示）
- 后端运行在 `http://localhost:8000`，前端运行在 `http://localhost:5173`。若遇到跨域请求（CORS）问题，可在 Django 中临时允许 CORS 或在 `vite.config.js` 中添加代理（proxy）将 API 请求转发到后端。
- 若需要，我可以帮你添加 `vite.config.js` 的代理示例或 Django 的 CORS 设置说明。

---

如果你希望我代为运行一次（例如启动后端或前端、或添加 proxy/CORS 示例），告诉我你要运行哪一端即可。 
