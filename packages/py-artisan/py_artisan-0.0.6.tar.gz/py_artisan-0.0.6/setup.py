from setuptools import setup, find_packages
import os

def read_requirements(filename):
    """读取 requirements 文件"""
    # 获取当前文件所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, filename)
    
    try:
        with open(filepath) as f:
            requirements = []
            for line in f:
                line = line.strip()
                # 跳过空行和注释
                if line and not line.startswith('#'):
                    requirements.append(line)
            return requirements
    except FileNotFoundError:
        # 如果文件不存在，返回空列表
        return []

setup(
    name="py_artisan",
    version="0.0.6",
    author="rokywang",
    author_email="wxytjustb@gmail.com",
    description="一个优雅好用的 Python 工具包",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wxytjustb/py-artisan",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=read_requirements('requirements/base.txt'),
    extras_require={
        "dev": read_requirements('requirements/dev.txt'),
    },
)