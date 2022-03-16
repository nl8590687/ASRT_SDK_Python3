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
ASRT语音识别Python SDK 语音识别接口调用类库
"""

import threading
import time
import wave
import requests
import numpy as np

from .Recorder import AudioRecorder
from .utils import *

def get_speech_recognizer(host:str, port:str, protocol:str):
    '''
    获取一个ASRT语音识别SDK接口调用实例对象 \\
    参数：\\
        host: 主机域名或IP.
        port: 主机端口号.
        protocol: 网络协议类型.
    '''
    if protocol.lower() == 'http' or protocol.lower() == 'https':
        return HttpSpeechRecognizer(host, port, protocol)
    return None


class BaseSpeechRecognizer():
    '''
    ASRT语音识别SDK接口调用类基类
    '''
    def __init__(self, host:str, port:str, protocol:str):
        self.host = host
        self.port = port
        self.protocol = protocol

    def recognite(self, wav_data, frame_rate, channels, byte_width):
        raise Exception("Method Unimpletment")
    
    def recognite_speech(self, wav_data, frame_rate, channels, byte_width):
        raise Exception("Method Unimpletment")
    
    def recognite_language(self, sequence_pinyin):
        raise Exception("Method Unimpletment")

    def recognite_file(self, filename):
        wave_data = read_wav_datas(filename)
        str_data = wave_data.str_data
        frame_rate = wave_data.sample_rate
        channels = wave_data.channels
        byte_width = wave_data.byte_width
        return self.recognite(wav_data=str_data,
                            frame_rate=frame_rate,
                            channels=channels,
                            byte_width=byte_width
                            )

class HttpSpeechRecognizer(BaseSpeechRecognizer):
    '''
    ASRT语音识别SDK基于HTTP协议接口调用类 \\
    参数: \\
        host: 主机域名或IP.
        port: 主机端口号.
        protocol: 网络协议类型.
        sub_path: 接口所在URL的子路径, 默认为""
    '''
    def __init__(self, host:str, port:str, protocol:str, sub_path:str=''):
        super().__init__(host, port, protocol)
        if protocol != 'http' and protocol != 'https':
            raise Exception('Unsupport netword protocol `' + protocol +'`')
        self._url_ = protocol + '://' + host + ':' + port
        self.sub_path = sub_path

    def recognite(self, wav_data, frame_rate:int, channels:int, byte_width:int) -> AsrtApiResponse:
        request_body = AsrtApiSpeechRequest(wav_data, frame_rate, channels, byte_width)
        headers = {'Content-Type': 'application/json'}
        response_object = requests.post(self._url_ + self.sub_path + '/all', headers=headers, data=request_body.to_json())
        response_body_dict = json.loads(response_object.text)
        response_body = AsrtApiResponse()
        response_body.from_json(**response_body_dict)
        return response_body
    
    def recognite_speech(self, wav_data, frame_rate, channels, byte_width):
        request_body = AsrtApiSpeechRequest(wav_data, frame_rate, channels, byte_width)
        headers = {'Content-Type': 'application/json'}
        response_object = requests.post(self._url_ + self.sub_path + '/speech', headers=headers, data=request_body.to_json())
        response_body_dict = json.loads(response_object.text)
        response_body = AsrtApiResponse()
        response_body.from_json(**response_body_dict)
        return response_body

    def recognite_language(self, sequence_pinyin):
        request_body = AsrtApiLanguageRequest(sequence_pinyin)
        headers = {'Content-Type': 'application/json'}
        response_object = requests.post(self._url_ + self.sub_path + '/language', headers=headers, data=request_body.to_json())
        response_body_dict = json.loads(response_object.text)
        response_body = AsrtApiResponse()
        response_body.from_json(**response_body_dict)
        return response_body

class SpeechRecognizer():
    def __init__(self, url_server = 'http://127.0.0.1:20000/', token_client = 'qwertasd'):
        self.url_server = url_server
        self.token_client = token_client

        self.IsRecognizing = False
        self.__func_callback__ = None
        self.__recorder__ = AudioRecorder()
        pass

    def SetCallbackFunction(self, func_callback):
        if(str(type(func_callback)) != "<class 'function'>"):
            raise TypeError('Parameter "func_callback" need the type of "function", but yours is "' + str(type(func_callback)) + '". ')
        self.__func_callback__ = func_callback

    def Start(self, interval = 6):
        if(self.__func_callback__ == None):
            raise ValueError('[ASRT SDK] You have not set callback function here. Please call function "SetCallbackFunction" to do this. ')
        t1 = threading.Thread(target=self.__thread_recognize__, args = (interval,))
        self.IsRecognizing = True
        t1.start()
        pass
    
    def __thread_recognize__(self, interval):
        self.__recorder__.Initialize()
        self.__recorder__.RecordAsync()
        while(True):
            time.sleep(interval)
            if(self.IsRecognizing == False):
                break
            wavs = self.__recorder__.GetAudioSamples()
            self.__recorder__.__clear_audio_buffer__()
            # test function
            #wavs = self.__test_function__()
            # test function
            t2 = threading.Thread(target = self.__post_to_server__, args=(wavs,))
            t2.start()
            

        pass

    def __post_to_server__(self, wavs, fs = 16000):

        datas={'token':self.token_client, 'fs':fs, 'wavs':wavs}
        r = requests.post(self.url_server, datas)
        r.encoding='utf-8'
        self.__func_callback__(text = r.text)
        pass

    def StopAsync(self):
        wavs = self.__recorder__.GetAudioSamples()
        self.__recorder__.StopRecording()
        self.IsRecognizing = False
        self.__recorder__.__clear_audio_buffer__()
        t2 = threading.Thread(target = self.__post_to_server__, args=(wavs,))
        t2.start()
        self.__recorder__.Close()
        pass

    def Stop(self):
        wavs = self.__recorder__.GetAudioSamples()
        self.__recorder__.StopRecording()
        self.IsRecognizing = False
        self.__recorder__.__clear_audio_buffer__()
        self.__post_to_server__(wavs)
        self.__recorder__.Close()
        pass

    def RecogniteFromFile(self, filename):
        wf = wave.open(filename, 'rb')
        num_frame = wf.getnframes()
        str_data=wf.readframes(num_frame)
        wave_data = np.fromstring(str_data, dtype = np.short) # 将声音文件数据转换为数组矩阵形式
        wave_data.shape = -1, wf.getnchannels() # 按照声道数将数组整形，单声道时候是一列数组，双声道时候是两列的矩阵
        wave_data = wave_data.T # 将矩阵转置
        self.__post_to_server__(wave_data[0], wf.getframerate())
        pass

    def __test_function__(self, filename = 'D:\\语音数据集\\ST-CMDS-20170001_1-OS\\20170001P00241I0052.wav'):
        '''
        测试用函数
        '''
        wf = wave.open(filename, 'rb')
        num_frame = wf.getnframes()
        str_data=wf.readframes(num_frame)
        wave_data = np.fromstring(str_data, dtype = np.short) # 将声音文件数据转换为数组矩阵形式
        wave_data.shape = -1, wf.getnchannels() # 按照声道数将数组整形，单声道时候是一列数组，双声道时候是两列的矩阵
        wave_data = wave_data.T # 将矩阵转置
        return wave_data[0]

