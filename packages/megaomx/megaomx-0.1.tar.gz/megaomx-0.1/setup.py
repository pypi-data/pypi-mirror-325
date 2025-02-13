from setuptools import setup, find_packages 

setup( name='megaomx',
       version = '0.1',
       packages=['om'],
       package=find_packages(),
       install_requires=['requests'],
       author='well4u',
       author_email='wellau@qq.com',
       description='The omx series control',
       license='MIT',
       keywords='megarobo om ovl',
       url='' )