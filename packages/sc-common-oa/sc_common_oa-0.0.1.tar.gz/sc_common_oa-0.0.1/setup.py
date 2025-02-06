from setuptools import setup, find_packages

setup(
    name='sc_common_oa',
    version='0.0.1',
    description='SC OA 接口修改信息',
    author='river',
    packages=find_packages(),
    install_requires=[
    "requests>=2.0.0",
    "jsonpath>=0.82",
             ],
)
