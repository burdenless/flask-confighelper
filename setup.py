"""
Flask-Config
-------------

Automatically loads environment configurations and checks required config variables are present
"""

from setuptools import setup

setup(
    name='Flask-Config',
    version='1.0',
    url='http://byt3smith.github.io/flask-config/',
    license='MIT License',
    author='Bob Argenbright',
    author_email='your-email@example.com',
    description='Handles loading environment configurations',
    long_description=__doc__,
    py_modules=['flask_config'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
