from setuptools import setup
from os.path import join, split

with open(join(split(__file__)[0], 'README.rst')) as f:
    long_description = f.read()

setup(
    name='botframework-python',
    version='0.1',

    description='A library to help write bots for botframework.com.',
    long_description=long_description,
    url='http://aka.ms/Python',

    # Author details
    author='Microsoft Corporation',
    author_email='python@microsoft.com',
    license='MIT License',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
    ],

    keywords='chat bot botframework',
    py_modules=['botframework'],
    install_requires=['aiohttp'],
)

