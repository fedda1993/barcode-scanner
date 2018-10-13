from setuptools import setup
setup(
    name = 'barcode',
    version = '0.1.0',
    packages = ['barcode'],
    entry_points = {
        'console_scripts': [
            'barcode = barcode.__main__:cli'
        ]
    })