import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-chatter',
    version='1.0.8',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='A WebSocket-based Chat app for Django developers.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://www.github.com/dibs-devs/chatter',
    author='Ahmed Ishtiaque, Dibs',
    author_email='ahmedishti27@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'channels==2.4.0',
        'bleach==3.1.0',
        'django>=3.0.1 ',
        'channels-redis==2.3.3',
    ]
)
