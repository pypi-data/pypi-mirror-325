from setuptools import setup

setup(
    name='dpysts',  # 模块名称
    version='0.0.1',      # 版本号
    packages=['dpysts'],  # 包含的Python包
    python_requires='>=3.8',  # 支持的Python版本
    install_requires=[],  # 依赖的外部库
    author='YUJING',  # 作者信息
    author_email='yujing@dianxiaomi.com',
    description='STS python client',  # 简短描述
    long_description=open('README.md', 'r').read(),  # 长描述（通常读取自README文件）
    long_description_content_type='text/markdown',  # 长描述类型
    url='https://github.com/your_username/your_package',  # 项目主页
    classifiers=[  # 项目分类标签
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
