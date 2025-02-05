from setuptools import setup, find_packages

setup(
    name="rse_api_client",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "setuptools",
        "requests",
        "python-dotenv",
    ],
    entry_points={
        'console_scripts': [
            'rse-api=rse_api_client.main:main',
        ],
    },
    include_package_data=True,
    description='A client for RSE API',
    author='Daniel Anzawa',
    author_email='danielanzawa@gmail.com',
    url='https://github.com/danicode/rse-api-client',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)