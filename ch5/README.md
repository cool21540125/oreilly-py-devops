# 套件管理


```bash
### Step0. 安裝套件管理工具
pip install setuptools twine
# twine 用來上傳 pkg 到 PyPI 的工具

### Step1. 寫 Code

### Step2. 寫 setup.py
# 

### Step3. 打包
rm -rf dist
rm -rf *.egg-info
python setup.py sdist

### Step4a. 本地使用 (直接從 "原始碼發佈" (也就是 tar) 做安裝)
pip install dist/hello_world_this_20240418-0.0.1.tar.gz

### Step4b. 上傳到 PyPI
twine upload --repository-url https://test.pypi.org/legacy/ dist/hello_world_this_20240418-0.0.1.tar.gz
# 需要到 PyPI 申請一組 API_TOKEN




```
