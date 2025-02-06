from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name            = 'timesTable',
    version         = '2.0.0',
    description='prints an N x N multiplication table',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url             = 'https://github.com/jrowellfx/timesTable',
    author          = 'James Philip Rowell',
    author_email    = 'james@alpha-eleven.com',

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Development Status :: 5 - Production/Stable',
    ],

    packages        = ['timesTable'],
    python_requires = '>=3.6, <4',
    install_requires=['python-baseconv>=1.2.2'],

    entry_points = {
        'console_scripts': [
            'times-table = timesTable.__main__:main',
        ]
    }
)
