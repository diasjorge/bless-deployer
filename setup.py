from setuptools import setup, find_packages

setup(
    name='bless_deployer',
    version='0.0.1',
    description='Deploy Bless to AWS',
    author='Jorge Dias',
    author_email='jorge@mrdias.com',
    url='',
    license="FreeBSD License",
    packages=find_packages(exclude=["test*", "data*"]),
    package_data={'bless_deployer': ['data/*.*']},
    install_requires=[
        'boto3',
        'configargparse'
    ],
    extras_require={
        'dev': [
            'zest.releaser[recommended]'
        ]
    },
    entry_points={
        'console_scripts': [
            'bless-deployer = bless_deployer.__main__:main'
        ]
    },
)
