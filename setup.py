#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2016-2099 Ailemon.net
#
# This file is part of ASRT Speech Recognition Tool Python SDK.
#
# ASRT is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# ASRT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ASRT.  If not, see <https://www.gnu.org/licenses/>.
# ============================================================================

"""
@author: nl8590687
ASRT语音识别Python SDK 安装
"""

try:
    from setuptools import setup #enables develop
except ImportError:
    from distutils.core import setup

from setuptools import find_packages

LONG_DESCRIPTION = '''
ASRT_SDK is a client sdk package for ASRT. 
ASRT is a high-level deep learning API for speech recognition,
written in Python and capable of running on top of
Keras, TensorFlow, or MxNet.
Use ASRT SDK if you need a speech recognition library that:
- Allows for easy and fast prototyping for speech recognition
  (through user friendliness, modularity, and extensibility).
- Supports both TensorFlow and other Deep learning framework(on future) for speech recognition.
- Applications can only run on CPU. 
- Can call ASRT api server module for developers to test models easily.
Read the documentation at: https://wiki.ailemon.net/docs/asrt-doc/asrt-doc-1dkgqc3871ktt
For a detailed overview of what makes ASRT special, see:
https://asrt.ailemon.net
ASRT is compatible with Python 3.0-3.10
and is distributed under the GPL v3.0 license.
'''

setup(name='asrt_sdk',
	version='1.1.1',
	description='A python sdk for ASRT Speech Recognition Toolkit',
	long_description=LONG_DESCRIPTION,
	long_description_content_type = 'text/markdown',
	author='ailemon',
	author_email='ailemon@ailemon.net',
	license='GPL v3.0',
	url='https://asrt.ailemon.net',
	download_url = "https://pypi.python.org/pypi/asrt_sdk",
	project_urls={
		"Bug Tracker": "https://github.com/nl8590687/ASRT_SDK_Python3/issues",
		"Documentation": "https://wiki.ailemon.net/docs/asrt-doc/asrt-doc-1dkgqc3871ktt",
		"Source Code": "https://github.com/nl8590687/ASRT_SDK_Python3",
	},
	python_requires='>=3.0',
	packages=find_packages(),
	package_data={
        '': ['LICENSE'], },
	zip_safe=False,
	install_requires=[
		'numpy',
		'wave',
		'requests',
	],

	classifiers=[
		'Intended Audience :: Developers',
		'Intended Audience :: Education',
		'Intended Audience :: Science/Research',
		('License :: OSI Approved :: '
         'GNU General Public License v3 or later (GPLv3+)'),
		"Operating System :: OS Independent",
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7'
	]
)
