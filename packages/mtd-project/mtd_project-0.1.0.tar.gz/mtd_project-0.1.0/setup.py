from setuptools import setup, find_packages

setup(
    name="mtd-project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",
    ],
    author="Chen",
    author_email="your.email@example.com",
    description="JDL经分看板数据处理工具",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Juziziju/MTD",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
) 