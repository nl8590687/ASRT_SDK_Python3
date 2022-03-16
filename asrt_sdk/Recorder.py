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
ASRT语音识别Python SDK 录音功能库
"""

import wave
from pyaudio import PyAudio, paInt16
import struct
import threading
import numpy as np


class AudioRecorder():
    def __init__(self, framerate = 16000, channels = 1, sampwidth = 2, num_frames_per_buffer = 2000):
        self.FrameRate = framerate
        self.Channels = channels
        self.SampleWidth = sampwidth
        self.__num_frames_per_buffer__ = num_frames_per_buffer

        self.__audio_buffers__ = []
        self.__stream__ = None
        self.IsRecording = False
        self.__rthread__ = None

        pass
    
    def Initialize(self):
        pa = PyAudio()
        self.__stream__ = pa.open(format = paInt16, channels = self.Channels, rate = self.FrameRate, input=True, frames_per_buffer = self.__num_frames_per_buffer__)

        pass

    def RecordAsync(self, time = -1):
        if(time < 0):
            time = 365 * 24 * 3600 # 录音一年，相当于无限
        self.__rthread__ = threading.Thread(target = self.__thread_record__, args=(time,))
        self.IsRecording = True
        self.__rthread__.start()
        pass

    def Record(self, time = 0):
        if(time < 0):
            raise ValueError('Record time shouldn\'t shorter than 0 s. ')
        self.__thread_record__(time)
        pass

    def __thread_record__(self, time = -1):
        count = 0
        while (count < time * (self.FrameRate // self.__num_frames_per_buffer__)): # 控制录音时间
            string_audio_data = self.__stream__.read(self.__num_frames_per_buffer__)
            #print(string_audio_data)
            self.__audio_buffers__.append(string_audio_data)
            count += 1
            print('[Recorder] Recording', count / 8, 's...', end='\r', flush=True)
            
            if(self.IsRecording == False):
                break
        print('[Recorder] Recorded ', count / 8, 's.               ', end='\n', flush=True)
        pass

    def StopRecording(self):
        self.IsRecording = False
        self.__rthread__.join()
        pass

    def SaveAudioToFile(self, filename):
        '''save the date to the wavfile'''
        wf=wave.open(filename,'wb')
        wf.setnchannels(self.Channels)
        wf.setsampwidth(self.SampleWidth)
        wf.setframerate(self.FrameRate)
        wf.writeframes(self.GetAudioStream())
        wf.close()
        pass

    def GetAudioStream(self):
        bytesStream = b"".join(self.__audio_buffers__)
        #print(bytesStream[-1000:])
        #f=open('test0.bin','wb')
        #f.write(bytesStream)
        #f.close()
        return bytesStream
    
    def GetAudioSamples(self):
        audio_bin_serials = self.GetAudioStream()
        wave_data = np.fromstring(audio_bin_serials, dtype = np.short) # 将声音文件数据转换为数组矩阵形式
        #print(wave_data[-1000:])
        return wave_data
        #return self.__audio_stream_to_short__(audio_bin_serials)
        pass
    
    def __audio_stream_to_short__(self, audio_stream):
        audio_bin_serials = audio_stream
        lst_sampels = []
        for i in range(len(audio_bin_serials) // self.SampleWidth):
            oneitem_bin = audio_bin_serials[i:i+2]
            oneitem_short = struct.unpack('h', oneitem_bin)
            lst_sampels.append(oneitem_short[0])
            pass
        return lst_sampels
    
    def __clear_audio_buffer__(self):
        self.__audio_buffers__ = []
        pass

    def Play(self):
        self.__play_audio__(self.GetAudioStream(), self.FrameRate, self.Channels, self.SampleWidth)
        pass
    
    def __play_audio__(self, audio_stream, framerate, channels, sampwidth):
        chunk=2014
        p=PyAudio()
        stream=p.open(format=p.get_format_from_width(sampwidth),channels=channels, rate=framerate,output=True)
        for i in range(0, len(audio_stream)//chunk):
            stream.write(audio_stream[i * chunk:(i+1) * chunk])
        stream.write(audio_stream[len(audio_stream)//chunk * chunk:])
        stream.close()
        p.terminate()
        pass

    def PlayFromFile(self, filename = '01.wav'):
        wf = wave.open(filename, 'rb')
        num_frame = wf.getnframes()
        data=wf.readframes(num_frame)
        self.__play_audio__(data[0],wf.getframerate(),wf.getnchannels(),wf.getsampwidth())
        pass

    def Close(self):
        self.__stream__.close()
        self.__stream__ = None
        self.__audio_buffers__ = []
        self.IsRecording = False
        self.__rthread__ = None
        pass

if (__name__ == '__main__'):
    import time
    rec = AudioRecorder()
    rec.Initialize()
    rec.RecordAsync()
    #buf=rec.GetAudioStream()
    #rec.SaveAudioToFile('01.wav')
    #buf = rec.GetAudioSamples()
    time.sleep(3)
    rec.StopRecording()
    buf = rec.GetAudioSamples()
    print(len(buf))
    rec.Play()

    rec.RecordAsync()
    time.sleep(3)
    rec.StopRecording()
    buf = rec.GetAudioSamples()
    print(len(buf))
    rec.Play()

    rec.Close()
    #print(buf)
    #print(type(buf),len(buf))
    
    #rec.PlayFromFile()
    
    pass