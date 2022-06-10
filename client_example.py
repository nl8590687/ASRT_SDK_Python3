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
ASRT语音识别服务Python SDK调用样例
"""

import asrt_sdk

# =========== use http protocol start =============
HOST = '127.0.0.1'
PORT = '20001'
PROTOCOL = 'http'
speech_recognizer = asrt_sdk.get_speech_recognizer(HOST, PORT, PROTOCOL)

FILENAME = 'A11_0.wav'
result = speech_recognizer.recognite_file(FILENAME)
print(result)
for index in range(0, len(result)):
    item = result[index]
    print("第", index, "段:", item.result)


wave_data = asrt_sdk.read_wav_datas(FILENAME)
result = speech_recognizer.recognite_speech(wave_data.str_data,
                                            wave_data.sample_rate,
                                            wave_data.channels,
                                            wave_data.byte_width)
print(result)
print(result.result)

result = speech_recognizer.recognite_language(result.result)
print(result)
print(result.result)
# =========== use http protocol end =============

# =========== use grpc protocol start =============
HOST = '127.0.0.1'
PORT = '20002'
PROTOCOL = 'grpc'
speech_recognizer = asrt_sdk.get_speech_recognizer(HOST, PORT, PROTOCOL)
FILENAME = 'A11_0.wav'
result = speech_recognizer.recognite_file(FILENAME)
print("wav文件识别结果:", result)

wave_data = asrt_sdk.read_wav_datas(FILENAME)
result = speech_recognizer.recognite_speech(wave_data.str_data,
                                            wave_data.sample_rate,
                                            wave_data.channels,
                                            wave_data.byte_width)
print("wav声学识别响应:", result)
print("wav声学识别结果:", result.result_data)

result = speech_recognizer.recognite_language(result.result_data)
print("语言模型识别响应:", result)
print("语言模型识别结果:", result.text_result)

result = speech_recognizer.recognite(wave_data.str_data,
                                            wave_data.sample_rate,
                                            wave_data.channels,
                                            wave_data.byte_width)
print("wav完整识别响应:", result)
print("wav完整识别结果:", result.text_result)

def make_wav_generator():
    for _ in range(2):
        yield wave_data.str_data, wave_data.sample_rate, wave_data.channels, wave_data.byte_width

stream_asr_text = ""
stream_buffer_text = ""

def callback_func(ret):
    global stream_asr_text
    global stream_buffer_text
    print("流式识别响应：", ret)
    print("流式识别结果：", ret.status_code, ret.text_result)
    if ret.status_code == 200000:
        stream_asr_text += ret.text_result
        stream_buffer_text = ""
    elif ret.status_code == 206000:
        stream_buffer_text = ret.text_result
    else:
        print("流式语音识别出错！", ret.status_code, ret.status_message)

    print("当前语音识别内容:", stream_asr_text+stream_buffer_text)

speech_recognizer.recognite_stream(make_wav_generator, 1, callback_func)

# =========== use grpc protocol end =============
