from setuptools import setup, find_packages

setup(
    name="kpi_evaluator",
    version="0.2.0",
    author="Phan Danh Đức",
    author_email="phanduc.ds@gmail.com",
    description="Thư viện đánh giá KPI nhân viên bằng AI",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dsphanduc",
    packages=find_packages(),
    install_requires=[
        "ollama"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)