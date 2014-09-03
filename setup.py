# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='django-sorl-hacks',
    version='0.1',
    author='Vladimir Savin',
    author_email='zero13cool@yandex.ru',

    description='Some usefull hacks based on sorl-thumbnail',
    long_description=open('README.rst').read(),
    url='https://github.com/zerc/sorl_hacks',
    license='MIT',

    packages=find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'django>=1.6',
        'sorl-thumbnail==11.12',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',

        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
