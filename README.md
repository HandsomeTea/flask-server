# flask-server
一个基于flask框架的http服务器，包含http服务器常用的基础代码，便于快速起一个python版的http服务器


启动
创建启动环境(虚拟环境)
conda create --name python3.8.10-flask-server python=3.8.10

使用python3.8.10-flask-server虚拟环境，vscode可在右下角选择(选项中没有所创建的虚拟环境可重启vscode)，其它终端控制台可激活虚拟环境使用：
conda activate python3.8.10-flask-server

安装依赖
pip install -r requirements.txt
启动
python -m flaskr

查看文档：
https://{host}/{base_path}/ui/

代码风格检查：
flake8 --config=tox.ini
