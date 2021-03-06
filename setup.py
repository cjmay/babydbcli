from setuptools import setup


__version__ = '0.1b3'


setup(
    name='babydbcli',
    version=__version__,
    description='little Dropbox CLI',
    scripts=['scripts/dbcp.py'],
    install_requires=[
        'dropbox>=2.2.0',
    ],
    url='https://github.com/cjmay/babydbcli',
    license='BSD',
)
