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

host = '127.0.0.1'
port = '20001'
protocol = 'http'
speech_recognizer = asrt_sdk.get_speech_recognizer(host, port, protocol)

filename = 'A11_0.wav'
result = speech_recognizer.recognite_file(filename)
print(result)
print(result.result)


wave_data = asrt_sdk.read_wav_datas(filename)
result = speech_recognizer.recognite_speech(wave_data.str_data,
                                            wave_data.sample_rate,
                                            wave_data.channels,
                                            wave_data.byte_width)
print(result)
print(result.result)

result = speech_recognizer.recognite_language(result.result)
print(result)
print(result.result)
