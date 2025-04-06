from setuptools import setup, find_packages

setup(
    name="cross_sectional_parameter_calculation",
    version="0.1.1",
    author="ManiacsTraitor",
    author_email="2727671635@QQ.COM",
    description="一个用以进行圆环截面参数计算的库，我主要是把它拿来算桩的相关问题",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)