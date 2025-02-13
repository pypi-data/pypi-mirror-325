import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='rpi_ws281x_disk',
    version='0.1.0',    
    description='A python library to control a collection of ws281x LED rings as a single disk',
    url='https://github.com/sypticus/rpi_ws281x_led_disk/',
    author='Kyle Hansen',
    author_email='sypticus@proton.me',
    packages=setuptools.find_packages(),
    license='BSD 2-clause',
    package_data={'': ['*.json']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    
    install_requires=[
        'rpi_ws281x'
    ],
    python_requires='>=3.6',
) 

