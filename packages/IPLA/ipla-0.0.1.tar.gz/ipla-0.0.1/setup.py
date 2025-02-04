from setuptools import setup, find_packages

setup(
    name='IPLA',
    version='0.0.1',
    author='Laogao',
    author_email='2983536011@qq.com',
    description='Incremental Probability Lottery Algorithm',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)