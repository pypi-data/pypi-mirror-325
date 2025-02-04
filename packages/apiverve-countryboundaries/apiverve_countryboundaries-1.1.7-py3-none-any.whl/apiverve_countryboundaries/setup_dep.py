from setuptools import setup, find_packages

setup(
    name='apiverve_countryboundaries',
    version='1.1.7',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Country Shapes is a simple tool for getting the shape of a specific country's border. It returns the shape of the specified country's border.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
