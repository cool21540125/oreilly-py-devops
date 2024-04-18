from setuptools import setup, find_packages

setup(
    name="hello-world",
    version="0.0.1",
    author="TonyChou",
    author_email="cool21540125@gmail.com",
    url="tonychoucc.com",
    description="A hello-world example package",
    packages=find_packages(),
    classifiers=[  # 底下這些稱之為 trove classifier, 有助於上傳到 PyPI 時, 能夠被有效的匹配
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
