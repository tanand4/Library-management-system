import os
from setuptools import setup, find_packages

from myapp import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = []

setup(
    name = "Library Management System",
    version = ".".join(map(str, __version__)),
    description = "",
    long_description = read('README.rst'),
    url = '',
    license = 'MIT',
    author = 'Tanmay,Caitlin,Himanshu',
    author_email = 'tanand4@hawk.iit.edu,cdavitt@hawk.iit.edu,hgarg1@hawk.iit.edu',
    packages = find_packages(exclude=['tests']),
    include_package_data = True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        #'Framework :: Django',
    ],
    install_requires = requirements,
    tests_require = [],
)
