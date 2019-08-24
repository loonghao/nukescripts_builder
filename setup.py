"""Describe our module distribution to Distutils."""

# Import third-party modules
from setuptools import setup

# Import local modules
import nukescripts_builder

setup(
    name='nukescripts_builder',
    author=nukescripts_builder.__author__,
    version=nukescripts_builder.__version__,
    author_email='hoolongvfx@gmail.com',
    url='',
    packages=['nukescripts_builder'],
    description='Build a Nuke scripts from a template.',
    entry_points={},
    install_requires=['quik'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.6'],
    package_data={'': ['LICENSE']},
)