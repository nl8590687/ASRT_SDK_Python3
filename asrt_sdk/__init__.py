'''@package processing
ASRT is a high-level deep learning API for speech recognition,
written in Python and capable of running on top of
Keras, TensorFlow, or MxNet.
Use ASRT if you need a deep learning library that:
- Allows for easy and fast prototyping for speech recognition
  (through user friendliness, modularity, and extensibility).
- Supports both Keras and other Deep learning framework(on future).
- Runs seamlessly on CPU and GPU.
- Contains a api server module for developers to test models easily.
Read the documentation at: https://github.com/nl8590687/ASRT_SpeechRecognition/wiki
For a detailed overview of what makes ASRT special, see:
https://asrt.ailemon.me
ASRT is compatible with Python 3.0-3.6
and is distributed under the GPL v3.0 license. 
'''
#from __future__ import absolute_import

from . import Recorder, SpeechRecognizer
from .Recorder import AudioRecorder
from .SpeechRecognizer import SpeechRecognizer
from .SpeechRecognizer import get_speech_recognizer, HttpSpeechRecognizer
from .utils import read_wav_datas

__version__ = '1.0.0'
