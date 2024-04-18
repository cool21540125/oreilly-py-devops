# 套件管理


```bash
pip install setuptools twine


ls
# README
# hello_world
# setup.py

### setup.py 撰寫完畢後, 打包~
python setup.py sdist


ls
# README
# hello_world
# setup.py
# dist                  <- 裡頭有 hello_world-${version}.tar.gz, 此為 "原始碼發佈"
# hello_world.egg-info  <- (尚未知)


### 可直接從上面的 "原始碼發佈" (也就是 tar) 做安裝
pip install dist/hello_world-0.0.1.tar.gz
```

# twine (上傳到 PyPI 新招)

上傳 python package 到 PyPI 的老舊方法為, 使用 setuptools 和 setup.py

而新一代的方式(不曉得 2024 的現在, 是否有其他更新的方法), 則是使用 twine

```bash
### 上傳到 test PyPI
twine upload --repository-url https://test.pypi.org/legacy/ dist/hello_world-0.0.1.tar.gz
# 需要到 PyPI 申請一組 API_TOKEN

```