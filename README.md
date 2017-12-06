## 介绍

	python 调用 apriso
	falcon + jsonrpc + apriso

## 安装

	git clone https://github.com/caizhengxin/apriso-falcon-jsonrpc.git

	pip install -r requirements.txt

## 配置

	[apriso]
    host = '192.168.209.128'
    operation = 'TONY'


	[server]
	    host = '0.0.0.0'
	    port = 8000

## 启动

	python app.py

## 测试

	python test.py

	返回json