from setuptools import setup, find_packages

with open("README", "r") as ff:
    long_description = ff.read()

setup(
    name="hello-world-this-20240418",  # 上傳到 PyPI 以後, 必須是 unique
    version="0.0.2",
    author="TonyChou",
    author_email="cool21540125@gmail.com",
    url="https://github.com/cool21540125/oreilly-py-devops",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="A hello-world example package",
    packages=find_packages(),
    classifiers=[  # 底下這些稱之為 trove classifier, 有助於上傳到 PyPI 時, 能夠被有效的匹配 (約定成俗的 Tags 啦)
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
