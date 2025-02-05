from setuptools import setup, find_packages

setup(
    name='fake-update',
    version='0.3',  # Make sure this is the new version
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'fake_update=fake_update.fake_update:main',  # Update to call main() function
        ],
    },
)
