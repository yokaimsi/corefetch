# setup.py

from setuptools import setup, find_packages

setup(
    name='corefetch',
    version='1.0.0',
    author='yokaimsi',
    author_email='contact.now.itachi@gmail.com',
    description='A powerful and fast system insights CLI tool with Sharingan ASCII art',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yokaimsi/corefetch',
    packages=find_packages(),
    py_modules=['corefetch'],
    install_requires=[
        'psutil',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'corefetch = corefetch:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
