
# Python package management - setuptools, setup.py, PyPI, twine, sdist, wheel

```bash
### Step0. 安裝套件管理工具
pip install setuptools  # 用來作 setup 打包的工具
pip install twine       # 用來做上傳到 PyPI 的工具
pip install wheel       # 用來因應 pip install 失敗的 Issue: https://github.com/pypa/pip/issues/12050


### Step 1. 寫 Code


### Step 2. 寫 setup.py


### Step 3. 打包
rm -rf dist
rm -rf *.egg-info
python setup.py sdist


### Step 4. 本地分享 tar 安裝使用 (直接從 "原始碼發佈" (也就是 tar) 做安裝)
pip install dist/hello_world_this_20240418-0.0.1.tar.gz


### Step 5A. 上傳到 PyPI
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# 需要到 PyPI 申請一組 API_TOKEN


### Setup 5B. 從 PyPI 下載安裝使用
pip install --index-url https://test.pypi.org/simple/hello_world_this_20240418


### 
```


# 其他 Linux Distributions 的使用

## Debin 

- 打包 .deb
- changelog
- control file
- debuild
- Debian repository - reprepro


## RPM

- spec file
- rpmbuild
- RPM repository - createrepo
