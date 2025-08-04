import os
from setuptools import setup

# 更可靠地获取当前目录
here = os.path.abspath(os.path.dirname(__file__))

# 读取文档
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# 自动获取描述（更健壮的方式）
description_line = next(line for line in long_description.splitlines() if line.strip())
description = description_line.strip()[1:-1]  # 移除首尾的装饰字符

setup(
    name='playsound',
    version='1.3.0',
    description=description,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/coder-free/playsound',
    author='Taylor Marks',
    author_email='taylor@marksfam.com',
    license='MIT',
    classifiers=[
        # ... (保留原有分类器)
    ],
    keywords='sound playsound music wave wav mp3 media song play audio',
    py_modules=['playsound'],  # 关键参数 - 指定单文件模块

    # 添加更多元数据
    python_requires='>=2.3, !=3.0.*, !=3.1.*',  # 根据实际支持情况调整
    entry_points={
        'console_scripts': [
            'playsound=playsound:main',  # 如果模块有main函数可这样添加
        ],
    },
)