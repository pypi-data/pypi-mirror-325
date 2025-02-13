from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='AioTonApi',
  version='0.1.1',
  author='vladdintov',
  author_email='example@gmail.com',
  description='',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/vladdintov/TonAPI/',
  packages=find_packages(),
  install_requires=['aiohttp>=3.11.11'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='tonapi aiotonapi jettonapi jetton ton',
  python_requires='>=3.7'
)