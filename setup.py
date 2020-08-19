
# -*- coding: utf-8 -*-
"""A module to send system sensor values to Home Assistant

See https://www.github.com/garethhowell/system_sensors
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import sys
from system_sensors import __version__

sys.path.insert(0, 'src')


def readme():
    with open('README.rst') as f:
        return f.read()


with open('LICENSE') as f:
    license = f.read()


setup(
    name='system_sensors',
    version=__version__,
    description='Collect data from Pi system sensors and send via mqtt',
    long_description=readme(),
    long_description_content_type='text/x-rst',
    url='https://www.github.com/garethhowell/system_sensors.git',
    author='Gareth Howell',
    author_email='gareth.howell@gmail.com',
    license=license,
    classifiers=[
		# How mature is this project? Common values are
    	#   3 - Alpha
    	#   4 - Beta
    	#   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
	    'Topic :: Other/Nonlisted Topic',
        'Operating System :: Raspbian'
	],
    keywords='raspbian python RaspberryPi',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'paho-mqtt==1.5.0',
        'psutil==5.6.6',
        'pytz==2019.2',
        'PyYAML==5.2'
        ],
    data_files=[
	    ('/etc/system_sensors', ['etc/system_sensors/settings.yaml.example']),
        ('/etc/systemd/system', ['etc/systemd/system_sensors.service'])
	],
    scripts=[
        'src/system_sensors/system_sensors.py'
    ]
)
