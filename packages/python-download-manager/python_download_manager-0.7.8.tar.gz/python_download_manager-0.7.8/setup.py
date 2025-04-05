from setuptools import setup, find_packages

import python_download_manager

setup(
    name='python-download-manager',
    version=python_download_manager.__version__,
    packages=find_packages(),
    install_requires=[
        # 列出你的模块依赖的其他包
        "requests",
        "py7zr",
        "tqdm",
        "unrar2-cffi"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    # 其他元数据
)
