from setuptools import setup, find_packages

setup(
    name='lightgboost',
    version='1.1.1',
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
    url='https://github.com/JPD-12/ironic-secureboot-driver',  # Update this with your actual URL
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

