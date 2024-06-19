from setuptools import setup, find_packages

setup(
    name='ransomware-security,
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'watchdog',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'my_project=main:main',
        ],
    },
    author='0625963141-cyber',
    author_email='cs7778503@github.com',
    description='Outil de protection contre les ransomwares',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/0625963141-cyber/ransomware-security/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
