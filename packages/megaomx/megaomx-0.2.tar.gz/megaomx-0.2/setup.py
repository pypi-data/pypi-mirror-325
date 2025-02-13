from setuptools import setup, find_packages 

setup( name='megaomx',
       version = '0.2',

       packages=find_packages( include=['om','om.*'] ),
       install_requires=['requests'],
       author='well4u',
       author_email='wellau@qq.com',
       description='The omx series control',
       license='MIT',
       keywords='megarobo om ovl',
       url='https://github.com/megarobo-open/omx.git' )