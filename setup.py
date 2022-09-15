from setuptools import find_packages, setup

with open("README.md") as file:
    read_me_description = file.read()


setup(
    name='py-stresser',
    version='2.0.0b2',
    author='gingersamurai',
    author_email='nazimmalyshev47@gmail.com',
    description='package for stress testing',
    long_description_content_type="text/markdown",
    long_description=read_me_description,
    url='https://github.com/gingersamurai/stresser',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'stresser=stresser.__main__:main'
        ]
    },
    include_package_data=True
)

