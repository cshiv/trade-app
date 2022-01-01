from setuptools import find_packages
from setuptools import setup

setup(
    name='TradeAlpha',
    version='0.1.0',
    install_requires=['app_config','controller'],
    packages=find_packages('aryabhata'),
    package_dir={'': 'aryabhata'},
    url='https://github.com/cshivas/trade-app',
    license='MIT',
    author='Chetan Shivashankar',
    author_email='chetu.10@gmail.com',
    description='Trade algo Version alpha'
)