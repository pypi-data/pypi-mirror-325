from setuptools import setup, find_packages

setup(
    name="MSanalyst",
    version="0.1.0",
    author="Wenchao Yu",
    author_email="2112007282@zjut.edu.cn",
    description="A tool for molecular networking and annotation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/WenchYu/MSanalyst",
    packages=find_packages(),  # 自动发现所有包
    include_package_data=True,
    package_data={
        'MSanalyst': ['msdb/*.csv', 'msdb/*.json'],
    },
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "MSanalyst-main=MSanalyst.main:main",
            "MSanalyst-mn_merging=MSanalyst.main:mn_merging",
            "MSanalyst-customized_db=MSanalyst.main:customized_db",
            "MSanalyst-ms2search=MSanalyst.main:ms2search",
            "MSanalyst-ms1search=MSanalyst.main:ms1search",
            "MSanalyst-re-networking=MSanalyst.main:re_networking",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires=">=3.8",
)