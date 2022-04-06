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
ASRT语音识别Python SDK 基础库模块
"""

import base64
import json
import wave
import numpy as np

class AsrtApiSpeechRequest:
    '''
    ASRT语音识别基于HTTP协议的API接口请求类(声学模型)
    '''
    def __init__(self, samples, sample_rate, channels, byte_width):
        self.samples = str(base64.urlsafe_b64encode(samples), encoding='utf-8')
        self.sample_rate = sample_rate
        self.channels = channels
        self.byte_width = byte_width

    def to_json(self):
        '''
        类转json
        '''
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True)

    def from_json(self, **entries):
        '''
        json转AsrtApiSpeechRequest
        '''
        self.__dict__.update(entries)

    def __str__(self):
        '''
        AsrtApiSpeechRequest转为字符串
        '''
        return self.to_json()

class AsrtApiLanguageRequest:
    '''
    ASRT语音识别基于HTTP协议的API接口请求类(声学模型)
    '''
    def __init__(self, sequence_pinyin):
        self.sequence_pinyin = sequence_pinyin

    def to_json(self):
        '''
        类转json
        '''
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True)

    def from_json(self, **entries):
        '''
        json转AsrtApiLanguageRequest
        '''
        self.__dict__.update(entries)

    def __str__(self):
        '''
        AsrtApiLanguageRequest转为字符串
        '''
        return self.to_json()

class AsrtApiResponse:
    '''
    ASRT语音识别基于HTTP协议的API接口响应类
    '''
    def __init__(self, status_code=0, status_message='', result=''):
        self.status_code = status_code
        self.status_message = status_message
        self.result = result
    def to_json(self):
        '''
        类转json
        '''
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True)

    def from_json(self, **entries):
        '''
        json转AsrtApiResponse
        '''
        self.__dict__.update(entries)

    def __str__(self):
        '''
        AsrtApiResponse转为字符串
        '''
        return self.to_json()

class WaveData:
    '''
    WAVE格式音频数据类
    '''
    def __init__(self, str_data, frame_rate, channels, byte_width) -> None:
        self.str_data = str_data
        self.sample_rate = frame_rate
        self.channels = channels
        self.byte_width = byte_width
        self.filename = ''

    def get_samples(self):
        '''
        str_data转short数组
        '''
        # 将声音文件数据转换为数组矩阵形式
        wave_data = np.fromstring(self.str_data, dtype = np.short)
        # 按照声道数将数组整形，单声道时候是一列数组，双声道时候是两列的矩阵
        wave_data.shape = -1, self.channels
        # 将矩阵转置
        wave_data = wave_data.T
        return wave_data

    def set_filename(self, filename):
        '''
        记录该wave文件名
        '''
        self.filename = filename

def read_wav_datas(filename):
    '''
    读取wave格式文件数据
    '''
    wav_file = wave.open(filename, 'rb')
    num_frame = wav_file.getnframes()
    str_data = wav_file.readframes(num_frame)
    frame_rate = wav_file.getframerate()
    channels = wav_file.getnchannels()
    byte_width = wav_file.getsampwidth()
    wav_file.close()
    return WaveData(str_data, frame_rate, channels, byte_width)
