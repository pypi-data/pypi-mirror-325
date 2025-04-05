from setuptools import setup, find_packages

setup(
    name='wqhelp',
    version='2.0.0',
    author='Avinion',
    author_email='shizofrin@gmail.com',
    description='Скрипт для получения информации о квестах в World of Warcraft',
    long_description=open('README.md').read(),
    url='https://x.com/Lanaev0li',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'wqhelp = wqhelp.wqhelp:main',
        ],
    },
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
)
