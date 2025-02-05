from setuptools import setup, find_packages

setup(
    name='amzlforecasting',
    version='0.1',
    packages=find_packages(),
    package_data={
        'data': ['data/*csv'],
    },
    install_requires=[
        'pandas',
    ],
    author="Jinwoo Je",
    auther_email="jeff.jw.je@gmail.com",
    description="common functions and datasets for AMZL forecasting",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/arahas/amzlforecasting",  # if you plan to use GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)