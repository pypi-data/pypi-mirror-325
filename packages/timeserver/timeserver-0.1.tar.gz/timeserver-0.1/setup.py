from setuptools import setup, find_packages

setup(
    name="timeserver",
    version="0.1",
    packages=find_packages(),
    install_requires=['flask'],
    entry_points={
        'console_scripts': [
            'timeserver=app:show_time',
        ],
    },
)



