from setuptools import setup, find_packages

setup(
    name='apiverve_dogbreeds',
    version='1.1.7',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Dog Breeds is a simple tool for getting information about dog breeds. It returns information such as breed name, temperament, lifespan, and more.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
