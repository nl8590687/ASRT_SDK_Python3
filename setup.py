try:
    from setuptools import setup #enables develop
except ImportError:
    from distutils.core import setup

from setuptools import find_packages

long_description = '''
ASRT_SDK is a client sdk package for ASRT. 
ASRT is a high-level deep learning API for speech recognition,
written in Python and capable of running on top of
Keras, TensorFlow, or MxNet.
Use ASRT SDK if you need a speech recognition library that:
- Allows for easy and fast prototyping for speech recognition
  (through user friendliness, modularity, and extensibility).
- Supports both Keras and other Deep learning framework(on future) for speech recognition.
- Applications can only run on CPU. 
- Can call ASRT api server module for developers to test models easily.
Read the documentation at: https://github.com/nl8590687/ASRT_SpeechRecognition/wiki
For a detailed overview of what makes ASRT special, see:
https://asrt.ailemon.me
ASRT is compatible with Python 3.0-3.6
and is distributed under the GPL v3.0 license.
'''

setup(name='asrt_sdk',
	version='1.0.0',
	description='A python client sdk for ASRT Deep-Learning-Based Auto Speech Recognition Toolkit',
	long_description=long_description,
	author='ailemon',
	author_email='ailemon@ailemon.me',
	license='GPL v3.0',
	url='https://asrt.ailemon.me',
	download_url = "https://pypi.python.org/pypi/asrt_sdk",
	project_urls={
		"Bug Tracker": "https://github.com/nl8590687/ASRT_SpeechRecognition/issues",
		"Documentation": "https://asrt.ailemon.me/docs",
		"Source Code": "https://github.com/nl8590687/ASRT_SpeechRecognition",
	},
	python_requires='>=3.0',
	packages=find_packages(),
	package_data={
        '': ['LICENSE'], },
	zip_safe=False,
	install_requires=[
		'numpy',
		'wave',
		'pyaudio',
		'requests',
	],
	
	classifiers=[
		'Intended Audience :: Developers',
		'Intended Audience :: Education',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: GPL v3.0 License',
		"Operating System :: OS Independent",
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6'
	]
)