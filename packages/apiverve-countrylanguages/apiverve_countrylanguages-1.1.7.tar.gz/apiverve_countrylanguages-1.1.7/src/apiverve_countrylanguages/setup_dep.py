from setuptools import setup, find_packages

setup(
    name='apiverve_countrylanguages',
    version='1.1.7',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Country Languages is a simple tool for getting the list of official and commonly spoken languages in a specific country.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
