from setuptools import setup

setup(
    name='fake-update',
    version='0.6',  # Update to the new version
    py_modules=['fake_update'],  # Explicitly include the fake_update module
    install_requires=[],
    entry_points={
        'console_scripts': [
            'fake_update=fake_update:main',  # Call the main() function
        ],
    },
)
