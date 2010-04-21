from setuptools import setup, find_packages
import os

NAME = 'pyong'
VERSION = '0.1'

# List your project dependencies here. See:
# http://packages.python.org/distribute/setuptools.html#declaring-dependencies
install_requires = [
]

def read_file(filename):
    here = os.path.abspath(os.path.dirname(__file__))
    return open(os.path.join(here, filename)).read()

setup(
    name=NAME,
    version=VERSION,
    description="One-player game, based on Pong.",
    long_description=read_file('README.rst'),
    keywords='game pong opengl pymunk pyglet',
    author='Jonathan Hartley',
    author_email='tartley@tartley.com',
    url='http://pypi.python.org/pypi/pyong',
    license='BSD',
    packages=find_packages(NAME),
    package_dir = {'': NAME},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['pyong=pyong:main']
    },
    # Get classifier strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
    ],
)

