from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name            = 'modTable',
    version         = '2.0.1',
    description='Prints addition and multiplication tables for Z mod n*Z',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url             = 'https://github.com/jrowellfx/modTable',
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

    packages        = ['modTable'],
    python_requires = '>=3.6, <4',

    entry_points = {
        'console_scripts': [
            'mod-table = modTable.__main__:main',
        ]
    }
)
