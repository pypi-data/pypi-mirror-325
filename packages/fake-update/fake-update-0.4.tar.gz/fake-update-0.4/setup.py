# setup.py
from setuptools import setup, find_packages

setup(
    name='fake-update',
    version='0.4',  # Update to the new version
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'fake_update=fake_update.fake_update:main',  # Call the main() function
        ],
    },
)
