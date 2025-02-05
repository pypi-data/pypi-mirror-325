from setuptools import setup, find_packages

setup(
    name='fake_update',
    version='0.2',
    packages=find_packages(),  # This automatically finds all packages inside the 'fake_update' folder
    install_requires=[],
    entry_points={
        'console_scripts': [
            'fake_update=fake_update.fake_update:fake_update',  # Make sure this points to the function inside fake_update.py
        ],
    },
)
