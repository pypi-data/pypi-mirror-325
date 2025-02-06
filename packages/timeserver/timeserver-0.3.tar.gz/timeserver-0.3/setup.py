from setuptools import setup, find_packages

setup(
    name="timeserver",
    version="0.3",  # Increment this version number
    packages=find_packages(),
    install_requires=['flask'],
    entry_points={
        'console_scripts': [
            'timeserver=timeserver.app:run_server',  # Ensure this function exists in app.py
        ],
    },
)

